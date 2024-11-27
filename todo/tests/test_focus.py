from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from todo.models import List, ListItem, Template, TemplateItem, ListTags, SharedList
import datetime
from django.utils import timezone
from todo.views import focus
from django.contrib.auth.models import User

class FocusViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='abc223',
            password='abc223',
            email='abc223@gmail.com'
        )
        
        self.list = List.objects.create(
            title_text="Testing_Focus",
            created_on=timezone.now(),
            updated_on=timezone.now(),
            user_id=self.user,
            is_shared=False
        )
        tags = ["Refreshing", "Learning", "Wellness", "Meeting", "Fitness", "Self Care", "Planning"]
        for tag in tags:
            List.objects.create(user_id=self.user, title_text=f"{tag} List", list_tag=tag, is_shared=False, created_on=timezone.now(),
            updated_on=timezone.now())


    def test_refreshing_tag(self):
        request = ''
        self.focus = focus(request)
        list_item = List.objects.filter(list_tag="Refreshing", user_id=self.user).first()
        self.assertIsNotNone(list_item, "No list found with tag 'Refreshing'")
        self.assertEqual(list_item.list_tag, "Refreshing", "The tag of the list is not 'Refreshing'")

    def test_learning_tag(self):
        request = ''
        self.focus = focus(request)
        list_item = List.objects.filter(list_tag="Learning", user_id=self.user).first()
        self.assertIsNotNone(list_item, "No list found with tag 'Learning'")
        self.assertEqual(list_item.list_tag, "Learning", "The tag of the list is not 'Learning'")

    def test_wellness_tag(self):
        request = ''
        self.focus = focus(request)
        list_item = List.objects.filter(list_tag="Wellness", user_id=self.user).first()
        self.assertIsNotNone(list_item, "No list found with tag 'Wellness'")
        self.assertEqual(list_item.list_tag, "Wellness", "The tag of the list is not 'Wellness'")

    def test_meeting_tag(self):
        request = ''
        self.focus = focus(request)
        list_item = List.objects.filter(list_tag="Meeting", user_id=self.user).first()
        self.assertIsNotNone(list_item, "No list found with tag 'Meeting'")
        self.assertEqual(list_item.list_tag, "Meeting", "The tag of the list is not 'Meeting'")

    def test_fitness_tag(self):
        request = ''
        self.focus = focus(request)
        list_item = List.objects.filter(list_tag="Fitness", user_id=self.user).first()
        self.assertIsNotNone(list_item, "No list found with tag 'Fitness'")
        self.assertEqual(list_item.list_tag, "Fitness", "The tag of the list is not 'Fitness'")

    def test_selfcare_tag(self):
        request = ''
        self.focus = focus(request)
        list_item = List.objects.filter(list_tag="Self Care", user_id=self.user).first()
        self.assertIsNotNone(list_item, "No list found with tag 'Self Care'")
        self.assertEqual(list_item.list_tag, "Self Care", "The tag of the list is not 'Self Care'")

    def test_planning_tag(self):
        request = ''
        self.focus = focus(request)
        list_item = List.objects.filter(list_tag="Planning", user_id=self.user).first()
        self.assertIsNotNone(list_item, "No list found with tag 'Planning'")
        self.assertEqual(list_item.list_tag, "Planning", "The tag of the list is not 'Planning'")

    