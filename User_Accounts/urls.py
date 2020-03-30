#This is to handel the Acounts data
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.Home.as_view(),name='Home'),
    path('home/',views.Home.as_view(),name='Home'),
    path('create/',views.Create_User.as_view(),name='Create_User'),
    path('update/',views.Update_User.as_view(),name='Update_User'),
    path('login/',views.Login_User.as_view(),name='login'),
    path('logout/',views.Logout_User,name='logout'),
    path('list/',views.Log_data,name='Detail'),


]
