import uuid
from django.utils.timezone import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import pre_save
from .CustomUserManager import *





# Create your models here.
class User(AbstractUser):
    id          = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    email       = models.EmailField(max_length=100,blank=False, null=False,unique=True)
    username    = models.CharField(max_length=50, blank=True ,null=True,unique=True)
    first_name  = models.CharField(max_length=50, blank=False, null=False)
    last_name   = models.CharField(max_length=50, blank=False, null=False)
    full_name   = models.CharField(max_length=100,blank=False, null=False)
    country     = models.CharField(max_length=50, blank=False,null=False)
    city        = models.CharField(max_length=50, blank=False,null=False)
    created_at  = models.DateTimeField(auto_now_add=datetime.now())
    updated_at  = models.DateTimeField(auto_now_add=False,auto_now=datetime.now())


    USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS=[email]


    def __str__(self):
        return self.full_name

    def activity_period(self):
        return self.log_activity.all()


    @property
    def activity_period(self):
        return self.log_activity.all()


    class Meta:
        db_table='Accounts'


@receiver(pre_save, sender=User)
def Create_user_full_name(sender, instance, *args, **kwargs):
    if not instance.full_name:
        instance.full_name = instance.first_name + ' ' + instance.last_name


class Log_Activity(models.Model):
    user        =models.ForeignKey(User , on_delete=models.CASCADE , related_name='log_activity')
    session_key = models.CharField(max_length=100,blank= True,null=True)
    start_time  = models.DateTimeField(blank=True,null=True)
    end_time    =models.DateTimeField(blank=True,null=True)


    class Meta:
        db_table='Log_Activity'
        ordering=['-start_time']

    def __str__(self):
        return self.user.last_name +' '+self.user.full_name