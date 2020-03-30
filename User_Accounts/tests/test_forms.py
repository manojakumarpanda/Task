# from User_Accounts.forms import *
# from django.test import SimpleTestCase
#
#
# class TestForms(SimpleTestCase):
#     def user_create_form(self):
#         form = User_form(data={
#             'username': 'demouser'
#             , 'email': 'demo2@email.com', 'password': 'demopassword',
#             'first_name': 'demo', 'last_name': 'user', 'country': 'india', 'city': 'mumbai'
#         })
#
#         self.assertTrue(form.is_valid())
#
#     def user_create_form_fail(self):
#         form = User_form(data={
#
#             'email': 'demo2@email.com', 'password': 'demopassword',
#             'first_name': 'demo', 'country': 'india', 'city': 'mumbai'
#         })
#
#         self.assertFalse(form.is_valid())
#         self.assertEquals(len(form.errors), 2)
#
#     def user_update_form(self):
#         form = User_Update_form(data={
#             'first_name': 'demo', 'last_name': 'user', 'country': 'india', 'city': 'mumbai'
#         })
#
#         self.assertTrue(form.is_valid())
#
#     def user_update_form_fail(self):
#         form = User_form(data={
#
#             'first_name': 'demo', 'country': 'india', 'city': 'mumbai'
#         })
#
#         self.assertFalse(form.is_valid())
#         self.assertEquals(len(form.errors), 1)
#
#
#     def user_update_blank_fail(self):
#         form = User_form(data={
#         })
#
#         self.assertFalse(form.is_valid())
#         self.assertEquals(len(form.errors), 4)
#
#
#     def user_login_form(self):
#
#         form = User_form(data={
#                 'username': 'demouser'
#                 , 'password': 'demopassword',
#             })
#
#         self.assertTrue(form.is_valid())
#
#
#     def user_login_form_fail(self):
#         form = User_form(data={
#
#             })
#
#         self.assertFalse(form.is_valid())
#         self.assertEquals(len(form.errors), 2)
#
#     def user_login_blank_fail(self):
#         form = User_form(data={'username':'demous'
#
#             })
#
#         self.assertFalse(form.is_valid())
#         self.assertEquals(len(form.errors), 1)

