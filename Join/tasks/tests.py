from django.test import TestCase
from rest_framework.test import APITestCase
from django.test import Client
from django.contrib.auth.models import User
from tasks.serializers import CategoryItemSerializer, ContactItemSerializer
from tasks.models import CategoryItem, ContactItem

class LoginTest(TestCase):
    def test_loginPass(self):
        self.client = Client()
        data={"email":'test_user@test.de',"password":'testuser',"username":"test_user"}
        self.user = User.objects.create_user(username='test_user', password='testuser', email='test_user@test.de')
        response = self.client.post('/login/',data)
        self.assertEqual(response.status_code, 200)
        
    def test_loginFailedByPassword(self):
        self.client = Client()
        data={"email":'test_user@test.de',"password":'testuser',"username":"test_user"}
        self.user = User.objects.create_user(username='test_user', password='testuse', email='test_user@test.de')
        response = self.client.post('/login/',data)
        self.assertEqual(response.status_code, 401)
        
    def test_loginFailedByEmail(self):
        self.client = Client()
        data={"email":'test_user@test.de',"password":'testuser',"username":"test_user"}
        self.user = User.objects.create_user(username='test_user', password='testuser', email='tes_user@test.de')
        response = self.client.post('/login/',data)
        self.assertEqual(response.status_code, 401)
        
class CategoriesTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',email='test@user.de', password='testuser')
        self.client.force_login(user=self.user)
        self.category = CategoryItem.objects.create(name='Test',color_key='#FFFFFF')
    def test_ListAllCategoriesAuthUser(self):
        
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code,200)
        serializer_data = CategoryItemSerializer([self.category],many=True).data
        self.assertEqual(response.data, serializer_data)
    
    def test_ListAllCategoriesNoAuthUser(self):
        self.client.logout()
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code,401)
        
    def test_create_Category(self):
        data = {
            'name':'Refactoring',
            'color_key':'#F1F2F3'
        }
        response = self.client.post('/categories/', data)
        self.assertEqual(response.status_code,201)
        category = CategoryItem.objects.get(name='Refactoring')
        self.assertEqual(response.data['name'],category.name)

class ContactsTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',email='test@user.de', password='testuser')
        self.client.force_login(user=self.user)
        self.contacts = ContactItem.objects.create(first_name='Test', last_name='Test', email='test@test.de', phone='0123484948')
    def test_ListAllContactsAuthUser(self):       
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code,200)
        serializer_data = ContactItemSerializer([self.contacts],many=True).data
        self.assertEqual(response.data, serializer_data)
    
    def test_ListAllCategoriesNoAuthUser(self):
        self.client.logout()
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code,401)
        
    def test_create_Contact(self):
        data = {
            'first_name':'Tester',
            'last_name':'Tester',
            'email':'test@test.de',
            'phone':'0123484948'
        }
        response = self.client.post('/contacts/', data)
        self.assertEqual(response.status_code,201)
        category = ContactItem.objects.get(first_name='Tester')
        self.assertEqual(response.data['first_name'],category.first_name)

