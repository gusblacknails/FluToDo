from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.views import LogoutView as UserLogout
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient
from .views import TaskListView, FluTodoLoginView, new_user, TaskDeleteView
from .api.views import LoginAPI, TaskCreateApi, TaskApi, CreateUserAPI, TaskUpdateApi, TaskDeleteApi
from django.contrib.auth.models import User
from .models import Task
import json
# URL's
class TestTaskListUrlWithoutLogin(TestCase):
        def test_task_list_page_status_code(self):
            response = self.client.get('/')
            self.assertEqual(response.status_code, 302)

        def test_task_list_page_response(self):
            response = self.client.get(reverse('home'))
            self.assertEqual(response.status_code, 302)


class TestTaskListUrl(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        

    def test_task_list_page_status_code(self):
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)

    def test_task_list_page_resolve(self):
       resolver = resolve('/')
       self.assertEqual(resolver.func.__name__, TaskListView.as_view().__name__)
    
    def test_task_list_page_response(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

class TestLoginUrl(TestCase):
   
    def setUp(self):
        self.credentials = {
            'username': 'testuser2',
            'password': '12345'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
    
    def test_login_user(self):
        self.user = User.objects.create_user(username='testuser3', password='12345')
        login = self.client.login(username='testuser2', password='12345')
        self.assertEqual(login, True)
        
    

    def test_task_list_page_resolve(self):
       resolver = resolve('/login/')
       self.assertEqual(resolver.func.__name__, FluTodoLoginView.as_view().__name__)
    
    def test_task_list_page_response(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        
class TestLogoutUrl(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser2',
            'password': '12345'}
    def test_logout(self):
        response = self.client.post('/logout/', self.credentials, follow=True)
        self.assertFalse(response.context['user'].is_active)
    
    def test_task_list_page_resolve(self):
        resolver = resolve('/logout/')
        self.assertEqual(resolver.func.__name__, UserLogout.as_view().__name__)

class TestSignUpUrl(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser4',
            'password1': '1a3d5v7w',
            'password2': '1a3d5v7w',
            'email':'flu@to.do'
            }
    def test_new_user(self):
        response = self.client.post('/signup/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
       
    
    def test_task_list_page_response(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_resolve(self):
        resolver = resolve('/signup/')
        self.assertEqual(resolver.func.__name__, "new_user")

# API TESTS

# Create User, Login, Logout
class TestTaskListApiWithoutLogin(TestCase):
   
    def test_task_list_page_status_code(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 401)

    def test_task_list_page_response(self):
        response = self.client.get(reverse('api_home'))
        self.assertEqual(response.status_code, 401)

class UserTestCase(TestCase):
    def setUp(self):
        user = User(
            email='gus@flu.todo',
            first_name='Testing',
            last_name='Testing',
            username='testing_login'
        )
        user.set_password('admin123')
        user.save()
        client = APIClient()
        response = client.post(
                '/api/login/', {
                'username': 'testing_login',
                'password': 'admin123',
            },
            format='json'
        )
        result = json.loads(response.content)
        self.access_token = result['token']
    def test_signup_user(self):


        client = APIClient()
        response = client.post(
                '/api/register/', {
                'email': 'testing@flutodo.com',
                'password': 'rc{4@qHjR>!b`yAV',
                'password_confirmation': 'rc{4@qHjR>!b`yAV',
                'username': 'testing1',
                "first_name":"Testing",
                "last_name":"Testing"
            },
            format='multipart'
        )

        self.assertEqual(response.status_code, 200)
        

    def test_login_user(self):
    
        client = APIClient()
        response = client.post(
                '/api/login/', {
                'username': 'testing_login',
                'password': 'admin123',
            },
            format='json'
        )
        result = json.loads(response.content)
        self.access_token = result['token']
        
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)
        self.assertIn('token', result)
    
    def test_logout_user(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.access_token)
        response = client.post('/api/logout/')
        self.assertEqual(response.status_code, 204)
    
    

    

