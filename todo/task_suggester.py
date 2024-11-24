from datetime import datetime, timedelta
from django.utils import timezone
from .models import ListItem

class TaskSuggester:
    def __init__(self, user_lists):
        self.user_lists = user_lists

    def get_priority_level(self, days_until_due):
        if days_until_due < 0:
            return "Critical Priority", "This task is overdue"
        elif days_until_due == 0:
            return "High Priority", "Due today - requires immediate attention"
        elif days_until_due <= 3:
            return "Medium Priority", "Due soon - plan to complete this task"
        elif days_until_due <= 7:
            return "Normal Priority", "Coming up this week"
        else:
            return "Low Priority", "Can be planned ahead"

    def calculate_task_priority(self, task):
        today = timezone.now().date()
        
        # Base priority score calculation
        priority_score = 0
        
        # Due date priority
        if task.due_date:
            days_until_due = (task.due_date - today).days
            if days_until_due < 0:  # Overdue
                priority_score = 100 + abs(days_until_due)  # Higher priority for more overdue
            elif days_until_due == 0:  # Due today
                priority_score = 90
            elif days_until_due <= 3:  # Due within 3 days
                priority_score = 80
            elif days_until_due <= 7:  # Due this week
                priority_score = 70
            else:
                priority_score = max(60 - days_until_due, 0)  # Gradually decreasing priority
            
            priority_level, reason = self.get_priority_level(days_until_due)
        else:
            priority_level = "No Due Date"
            reason = "No deadline set"
            
        return priority_score, priority_level, reason

    def get_suggested_tasks(self, max_limit=6):
        incomplete_tasks = ListItem.objects.filter(
            list__in=self.user_lists,
            is_done=False
        ).select_related('list')
        
        task_priorities = [
            (task, *self.calculate_task_priority(task))
            for task in incomplete_tasks
        ]
        
        # Sort by:
        # 1. Priority score (highest first)
        # 2. Due date (earlier first)
        # 3. Creation date (older first) for tasks due on same date
        sorted_tasks = sorted(
            task_priorities,
            key=lambda x: (
                x[1],  # Priority score
                x[0].due_date if x[0].due_date else timezone.now().date() + timezone.timedelta(days=365),  # Due date
                x[0].created_on  # Creation date for same-day tasks
            ),
            reverse=True
        )
        
        # Filter high and critical priority tasks
        urgent_tasks = [(task, priority_level, reason) 
                       for task, _, priority_level, reason in sorted_tasks 
                       if priority_level in ['Critical Priority', 'High Priority']]
        
        # If we have more than max_limit urgent tasks, show all of them
        if len(urgent_tasks) > max_limit:
            return urgent_tasks
        
        # Otherwise, return up to max_limit tasks including other priorities
        return [(task, priority_level, reason) 
                for task, _, priority_level, reason in sorted_tasks[:max_limit]]