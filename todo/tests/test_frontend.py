from django.urls import reverse
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.utils import timezone
from todo.models import List, ListItem, Template, ListTags
from django.contrib.messages.storage.fallback import FallbackStorage
from todo.views import login_request, getListTagsByUserid
import json

class FrontendTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', 
            email='jacob@example.com', 
            password='top_secret'
        )
        self.client.login(username='jacob', password='top_secret')
        
        self.list = List.objects.create(
            title_text="Test List",
            created_on=timezone.now(),
            updated_on=timezone.now(),
            user_id=self.user,
            is_shared=False
        )

    def test_login_request(self):
        """Test login functionality"""
        request = self.factory.post('/login/')
        request.user = self.user
        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))
        response = login_request(request)
        self.assertEqual(response.status_code, 200)

    def test_create_new_todo_list(self):
        """Test list creation"""
        test_data = {
            'list_name': 'test',
            'create_on': 1670292391,
            'list_tag': 'test_tag',
            'shared_user': '',
            'create_new_tag': True
        }
        response = self.client.post(
            reverse('todo:createNewTodoList'),
            data=json.dumps(test_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)

    def test_add_new_list_item(self):
        """Test adding new item to list"""
        params = { 
            'list_id': self.list.id,
            'list_item_name': "random", 
            'create_on': 1670292391,
            'due_date': "2023-01-01",
            'tag_color': "#f9f9f9",
            'item_text': "",
            'is_done': False
        }
        response = self.client.post(
            reverse('todo:addNewListItem'),
            data=json.dumps(params),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)

    def test_remove_list_item(self):
        """Test list item deletion"""
        item = ListItem.objects.create(
            list=self.list,
            item_name="Test Item",
            created_on=timezone.now(),
            due_date=timezone.now().date()
        )
        response = self.client.post(
            reverse('todo:removeListItem'),
            data=json.dumps({'list_item_id': item.id}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 302)
 
    def test_todo_from_template(self):
        """Test creating list from template"""
        template = Template.objects.create(
            title_text="Test Template",
            created_on=timezone.now(),
            updated_on=timezone.now(),
            user_id=self.user
        )
        response = self.client.post(
            reverse('todo:todo_from_template'),
            {'template': template.id}
        )
        self.assertEqual(response.status_code, 302)

    def test_get_list_tags(self):
        """Test retrieving user's list tags"""
        request = self.factory.get('/todo/')
        request.user = self.user
        ListTags.objects.create(
            user_id_id=self.user.id,
            tag_name='test',
            created_on=timezone.now()
        )
        post = request.POST.copy()
        post['todo'] = 1
        request.POST = post
        request.method = "POST"
        response = getListTagsByUserid(request)
        self.assertIsNotNone(response)

    def test_mark_list_item(self):
        """Test marking item as complete"""
        item = ListItem.objects.create(
            list=self.list,
            item_name="Test Item",
            created_on=timezone.now(),
            due_date=timezone.now().date()
        )
        response = self.client.post(
            reverse('todo:markListItem'),
            data=json.dumps({
                'list_id': self.list.id,
                'list_item_id': item.id,
                'list_item_name': item.item_name,
                'rating': 5,
                'is_done': True,
                'finish_on': int(timezone.now().timestamp())
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
  