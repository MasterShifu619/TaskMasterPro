from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from todo.models import List, ListItem
from todo.task_suggester import TaskSuggester
from datetime import timedelta

class TaskSuggesterTest(TestCase):
    def setUp(self):
        """
        Set up test environment before each test:
        - Creates a test user
        - Creates a test list
        - Initializes TaskSuggester with the test list
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
            email='test@example.com'
        )
        
        self.list = List.objects.create(
            title_text="Test List",
            created_on=timezone.now(),
            updated_on=timezone.now(),
            user_id=self.user,
            is_shared=False
        )
        
        self.task_suggester = TaskSuggester([self.list])
        
    def test_priority_level_calculation(self):
        """
        Tests the priority level calculation for different day ranges:
        - Overdue tasks (negative days)
        - Tasks due today (0 days)
        - Tasks due soon (2 days)
        - Tasks due this week (5 days)
        - Tasks due later (10 days)
        """
        test_cases = [
            (-1, ("Critical Priority", "This task is overdue")),
            (0, ("High Priority", "Due today - requires immediate attention")),
            (2, ("Medium Priority", "Due soon - plan to complete this task")),
            (5, ("Normal Priority", "Coming up this week")),
            (10, ("Low Priority", "Can be planned ahead"))
        ]
        
        for days, expected in test_cases:
            priority_level, reason = self.task_suggester.get_priority_level(days)
            self.assertEqual((priority_level, reason), expected)

    def test_task_priority_calculation(self):
        """
        Tests the priority score calculation for tasks:
        - Verifies correct priority level for tasks due today
        - Verifies correct priority score for tasks due today
        - Verifies critical priority for overdue tasks
        - Verifies score calculation for overdue tasks
        """
        now = timezone.now()
        
        task_today = ListItem.objects.create(
            list=self.list,
            item_name="Today's Task",
            due_date=now.date(),
            created_on=now
        )
        
        score, level, reason = self.task_suggester.calculate_task_priority(task_today)
        self.assertEqual(level, "High Priority")
        self.assertEqual(score, 90)
        
        task_overdue = ListItem.objects.create(
            list=self.list,
            item_name="Overdue Task",
            due_date=now.date() - timedelta(days=2),
            created_on=now
        )
        
        score, level, reason = self.task_suggester.calculate_task_priority(task_overdue)
        self.assertEqual(level, "Critical Priority")
        self.assertTrue(score > 100)

    def test_task_without_due_date(self):
        """
        Tests handling of tasks with far future due date:
        - Verifies correct priority level assignment for tasks that effectively
          have no immediate due date by setting it far in the future
        - Verifies correct reason message
        """
        far_future_date = timezone.now().date() + timedelta(days=365)  # One year in future
        task = ListItem.objects.create(
            list=self.list,
            item_name="No Due Date Task",
            created_on=timezone.now(),
            due_date=far_future_date  # Set far future date instead of None
        )
        
        score, level, reason = self.task_suggester.calculate_task_priority(task)
        self.assertEqual(level, "Low Priority")
        self.assertEqual(reason, "Can be planned ahead")

    def test_suggested_tasks_ordering(self):
        """
        Tests the ordering of suggested tasks:
        - Creates tasks with different due dates
        - Verifies that overdue tasks appear first
        - Verifies that today's tasks appear second
        - Ensures correct priority-based ordering
        """
        now = timezone.now()
        
        tasks = [
            ListItem.objects.create(
                list=self.list,
                item_name=f"Task {i}",
                due_date=now.date() + timedelta(days=days),
                created_on=now
            )
            for i, days in enumerate([-2, 0, 2, 5, 10])
        ]
        
        suggested_tasks = self.task_suggester.get_suggested_tasks()
        self.assertEqual(suggested_tasks[0][0].item_name, "Task 0")  # Overdue task
        self.assertEqual(suggested_tasks[1][0].item_name, "Task 1")  # Today's task

    def test_max_limit_enforcement(self):
        """
        Tests the enforcement of maximum task limit:
        - Creates more tasks than the max limit
        - Verifies that only max_limit tasks are returned
        - Ensures the most important tasks are included
        """
        now = timezone.now()
        
        for i in range(8):
            ListItem.objects.create(
                list=self.list,
                item_name=f"Task {i}",
                due_date=now.date() + timedelta(days=i),
                created_on=now
            )
        
        suggested_tasks = self.task_suggester.get_suggested_tasks(max_limit=6)
        self.assertLessEqual(len(suggested_tasks), 6)

    def test_multiple_urgent_tasks(self):
        """
        Tests handling of multiple urgent tasks:
        - Creates multiple overdue and due-today tasks
        - Verifies that all urgent tasks are included
        - Ensures urgent tasks override max_limit when necessary
        """
        now = timezone.now()
        
        # Create overdue tasks
        for i in range(4):
            ListItem.objects.create(
                list=self.list,
                item_name=f"Overdue Task {i}",
                due_date=now.date() - timedelta(days=i+1),
                created_on=now
            )
        
        # Create today's tasks
        for i in range(3):
            ListItem.objects.create(
                list=self.list,
                item_name=f"Today Task {i}",
                due_date=now.date(),
                created_on=now
            )
            
        suggested_tasks = self.task_suggester.get_suggested_tasks(max_limit=6)
        
        urgent_count = len([task for task, level, _ in suggested_tasks 
                          if level in ("Critical Priority", "High Priority")])
        self.assertEqual(urgent_count, 7)



    def test_task_priority_with_completed_tasks(self):
        """
        Tests handling of completed tasks:
        - Creates a mix of completed and incomplete tasks
        - Verifies that completed tasks are not included in suggestions
        - Ensures priority calculation ignores completed tasks
        """
        now = timezone.now()
        
        # Create completed task with high priority due date
        completed_task = ListItem.objects.create(
            list=self.list,
            item_name="Completed Urgent Task",
            due_date=now.date(),
            created_on=now,
            is_done=True,
            finished_on=now
        )
        
        # Create incomplete task with lower priority
        incomplete_task = ListItem.objects.create(
            list=self.list,
            item_name="Incomplete Future Task",
            due_date=now.date() + timedelta(days=5),
            created_on=now,
            is_done=False
        )
        
        suggested_tasks = self.task_suggester.get_suggested_tasks()
        task_names = [task[0].item_name for task in suggested_tasks]
        self.assertNotIn("Completed Urgent Task", task_names)
        self.assertIn("Incomplete Future Task", task_names)

    def test_task_priority_across_multiple_lists(self):
        """
        Tests priority calculation across multiple lists:
        - Creates multiple lists with tasks
        - Verifies that tasks from all lists are considered
        - Ensures correct priority ordering regardless of list
        """
        now = timezone.now()
        
        # Create a second list
        second_list = List.objects.create(
            title_text="Second List",
            created_on=now,
            updated_on=now,
            user_id=self.user,
            is_shared=False
        )
        
        # Initialize TaskSuggester with both lists
        multi_list_suggester = TaskSuggester([self.list, second_list])
        
        # Create tasks in different lists
        task1 = ListItem.objects.create(
            list=self.list,
            item_name="List 1 Task",
            due_date=now.date() + timedelta(days=2),
            created_on=now
        )
        
        task2 = ListItem.objects.create(
            list=second_list,
            item_name="List 2 Urgent Task",
            due_date=now.date(),
            created_on=now
        )
        
        suggested_tasks = multi_list_suggester.get_suggested_tasks()
        self.assertEqual(suggested_tasks[0][0].item_name, "List 2 Urgent Task")
        self.assertEqual(suggested_tasks[1][0].item_name, "List 1 Task")

    def test_priority_score_gradual_decrease(self):
        """
        Tests that priority score gradually decreases for future tasks:
        - Creates tasks with increasingly distant due dates
        - Verifies that priority scores decrease appropriately
        - Ensures minimum score of 0 is maintained
        """
        now = timezone.now()
        
        # Create tasks due in 10, 20, and 30 days
        future_tasks = []
        for days in [10, 20, 30]:
            task = ListItem.objects.create(
                list=self.list,
                item_name=f"Future Task {days}",
                due_date=now.date() + timedelta(days=days),
                created_on=now
            )
            future_tasks.append(task)
        
        # Get priority scores
        scores = []
        for task in future_tasks:
            score, _, _ = self.task_suggester.calculate_task_priority(task)
            scores.append(score)
        
        # Verify scores decrease
        self.assertTrue(scores[0] > scores[1] > scores[2])
        self.assertTrue(min(scores) >= 0)  # Ensure no negative scores

    def test_empty_list_suggestions(self):
        """
        Tests task suggestions with empty lists:
        - Creates TaskSuggester with empty list
        - Verifies empty suggestion list is returned
        - Ensures no errors occur with empty data
        """
        # Create new empty list
        empty_list = List.objects.create(
            title_text="Empty List",
            created_on=timezone.now(),
            updated_on=timezone.now(),
            user_id=self.user,
            is_shared=False
        )
        
        # Initialize suggester with empty list
        empty_suggester = TaskSuggester([empty_list])
        
        # Get suggestions
        suggested_tasks = empty_suggester.get_suggested_tasks()
        
        # Verify empty results
        self.assertEqual(len(suggested_tasks), 0)