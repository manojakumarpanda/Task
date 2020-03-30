# from django.test import TestCase
# from User_Accounts.models import User,Log_Activity
# from django.utils.timezone import datetime
# import time
#
#
# class TestModel(TestCase):
#     def setUp(self) :
#         self.user1=User.objects.create(username='demouser2', email='demo2@email.com', password='demopassword',
#                             first_name='demo', last_name='user', country='india', city='mumbai')
#         self.created=datetime.now()
#         self.log=Log_Activity.objects.create(user=self.user1,start_time=datetime.now())
#         time.sleep(50)
#         self.log2=Log_Activity.objects.create(user=self.user1,start_time=datetime.now())
#
#     def assign_the_fullname(self):
#         self.assertEquals(self.user1.full_name,'demo user')
#         self.count=User.objects.all()
#         self.assertEquals(len(self.count),1)
#
#     def log_user(self):
#         self.assertEquals(self.log.start_time,self.created)
#         self.assertEquals(len(Log_Activity.objects.filter(user__id=self.user1.id)),2)