# from django.test import TestCase,Client
# from django.urls import reverse
# from User_Accounts.models import *
# import json
#
#
# class TestView(TestCase):
#     def Setup(self):
#         self.client=Client()
#         self.home_url=reverse('Home')
#         self.Home_url=reverse('home')
#         self.create_url=reverse('Create_User')
#         self.update_url=reverse('Update_User')
#         self.login_url=reverse('login')
#         self.logout_url=reverse('logout')
#         self.detail_url=reverse('Detail')
#
#         User.objects.create(username='demouser', email='demo@email.com', password='demopassword',
#                             first_name='demo', last_name='user', country='india', city='mumbai')
#
#
#     def test_project_list_GET(self):
#         response=self.client.get(self.home_url)
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,'Accounts/home.html')
#
#     def test_project_GET(self):
#         response=self.client.get(self.home_url)
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,'Accounts/home.html')
#
#     def test_Create_user_GET(self):
#         response = self.client.get(self.create_url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'Accounts/User_creat.html')
#
#     def test_Update_GET(self):
#         response=self.client.get(self.update_url)
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,'Accounts/Update_user.html')
#
#     def test_login_GET(self):
#         response=self.client.get(self.login_url)
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,'Accounts/login.html')
#
#     def test_detail_GET(self):
#         response=self.client.get(self.home_url)
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,'Activity/home.html')
#
#     def test_project_post(self):
#         response=self.client.post(self.create_url)
#
#         User.objects.create(username='demouser1', email='demo1@email.com', password='demopassword1',
#                             first_name='demo', last_name='user', country='india', city='mumbai')
#         self.assertEqual(response.status_code,302)
#
#
#
#
#
#
#
