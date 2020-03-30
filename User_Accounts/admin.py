from django.contrib import admin
from .models import User,Log_Activity


# Register your models here.
class User_Admin(admin.ModelAdmin):
    list_display = ['email','first_name','last_name']
    list_filter = ['email','first_name']

admin.site.register(User,User_Admin)


# Register your models here.
class Log_Admin(admin.ModelAdmin):
    list_display = ['id','start_time']

admin.site.register(Log_Activity,Log_Admin)