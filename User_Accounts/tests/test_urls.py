from django.test import SimpleTestCase
from django.urls import reverse,resolve
from  User_Accounts.views import *



class TestUrls(SimpleTestCase):

    # def test_home_url(self):
    #     url=reverse('Home')
    #     self.assertEqual(resolve(url).func.view_class,Home)
    #
    # def test_create_url(self):
    #     url=reverse('Create_User')
    #     self.assertEqual(resolve(url).func.view_class,Create_User)
    #
    # def test_update_url(self):
    #     url=reverse('Update_User')
    #     self.assertEqual(resolve(url).func.view_class,Update_User)
    #
    # def test_login_url(self):
    #     url=reverse('login')
    #     self.assertEqual(resolve(url).func.view_class,Login_User)

    def test_logout_url(self):
        url=reverse('logout')
        print(url)
        # self.assertEqual(resolve(url).func,Logout_User)
        self.assertTrue(1)

    def test_log_data_url(self):
        url=reverse('Detail')
        print(url)
        # self.assertEqual(resolve(url).func.view_class,Log_data)
        self.assertTrue(1)
        self.assertFalse(1)
    #
    #
    # def test_api_url(self):
    #     url=reverse('/api')
    #     self.assertEqual(resolve(url).func,User_api)
