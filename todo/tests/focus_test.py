from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from todo.models import List, ListItem, Template, TemplateItem, ListTags, SharedList
import datetime

class FocusViewTests(TestCase):

    def setUp(self):
        # Creating two users for testing
        self.user1 = User.objects.create_user(username='test1', password='test1password', email='test1@gmail.com')
        x = self.client.login(username='test1', password='test1password') 
        self.assertTrue(x, "User1 should be able to log in with valid credentials.")
        tags = ["Refreshing", "Learning", "Wellness", "Meeting", "Fitness", "Self Care", "Planning"]
        for tag in tags:
            List.objects.create(user_id=self.user1, title_text=f"{tag} List", list_tag=tag)


    def test_status(self):
        #Retrieve URL of focus.html from urls.py
        response1 = self.client.get(reverse('focus')) 
        self.assertEqual(response1.status_code, 200)  
        self.assertContains(response1, "Your Lists for Today!")
        self.assertContains(response1, "It's Planning Sunday!")
        self.assertContains(response1, "It's Planning Sunday!")
        self.assertContains(response1, "It's Fitness Friday!")
        self.assertContains(response1, "It's Self-Care Saturday!")

    def test_tags(self):
        today_num = datetime.datetime.now().weekday()
        tags = {
            0: "Refreshing",
            1: "Learning",
            2: "Wellness",
            3: "Meeting",
            4: "Fitness",
            5: "Self-Care",
            6: "Planning",
        }
        #For the current day
        expected_tag = tags.get(today_num)
        response = self.client.get(reverse('focus'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, expected_tag)

        today_num = 0
        expected_tag = tags.get(today_num)
        response = self.client.get(reverse('focus'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, expected_tag)

        today_num = 2
        expected_tag = tags.get(today_num)
        response = self.client.get(reverse('focus'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, expected_tag)

        today_num = 3
        expected_tag = tags.get(today_num)
        response = self.client.get(reverse('focus'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, expected_tag)

        today_num = 5
        expected_tag = tags.get(today_num)
        response = self.client.get(reverse('focus'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, expected_tag)
        

x1 = FocusViewTests()
x1.setUp()
x1.test_status()
x1.test_tags()
