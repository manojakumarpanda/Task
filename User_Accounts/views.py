from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.views.generic import View,UpdateView
from .forms import  User_form,User_login,User_Update_form
from .models import User,Log_Activity
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from rest_framework import viewsets
from .serialisers import User_serialiser
from django.contrib.auth.decorators import login_required
from rest_framework import permissions
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.

class Home(View):

    def get(self, request, *args, **kwargs):
        context={'title':'home Page'}
        return render(request,'Accounts/home.html',context=context)

@login_required(login_url='/accounts/login/')
def Log_data(request):
    print(request.user.id)
    data=Log_Activity.objects.filter(user__id=request.user.id)
    print(data)
    return render(request,'Activity/home.html',{'data':data})

class User_api(viewsets.ModelViewSet):
    serializer_class = User_serialiser
    queryset         = User.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class Create_User(View):
    form_class      =User_form
    template_name   ='Accounts/User_creat.html'

    def get(self,request,*args,**kwargs):
        template    =self.template_name
        context     ={'title':'User From','form':self.form_class}
        return render(request,template,context=context)

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST or None)
        try:
            if form.is_valid():
                user = User(email       =form.cleaned_data['email']     ,username  =form.cleaned_data['username'],
                            first_name  =form.cleaned_data['first_name'],last_name =form.cleaned_data['last_name'],
                            country     =form.cleaned_data['country'],   city      =form.cleaned_data['city']
                            )
                user.set_password(raw_password=form.cleaned_data['password'])
                user.save()
                messages.success(request,'The user is created successfully')
                return HttpResponseRedirect('/')
            if form.errors:
                return messages.ERROR
        except AttributeError:
            raise messages.ERROR(request, 'There is some error try latter')

        context = self.context = {'form':form, 'title': 'User_add form'}
        return render(request, self.template_name, context=context)


#for the user login
class Login_User(View):
    form_class      =User_login
    template_name   ='Accounts/login.html'

    def get(self,request,*args,**kwargs):
        context ={'title':'Login','form':self.form_class}
        template=self.template_name
        return render(request,template,context=context)

    def post(self,request,*args,**kwargs):
        form    =self.form_class(request.POST or None)
        context = {'title': 'Login', 'form': form}
        template=self.template_name
        if form.is_valid():
            uname=form.cleaned_data['username']
            try:
                global username
                username    =uname
                username    =User.objects.get(email=username)
            except User.DoesNotExist:
                username    =form.cleaned_data['username']
            user =authenticate(username=username,
                              password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                data    =User.objects.get(id=request.user.id)
                log_data=Log_Activity.objects.filter(user__id=request.user.id)
                context ={'userdata':data,'log_data':log_data}
                return render(request,'Accounts/home.html',context=context)
        return render(request,template,context=context)



@login_required(login_url='/accounts/login/')
def Logout_User(request):
    logout(request)
    return HttpResponseRedirect('/')

@method_decorator(login_required,name='dispatch')
class Update_User(UpdateView):
    form_class = User_Update_form

    def get(self,requset,**kwargs):
        data=User.objects.get(id=requset.user.id)
        print(data)
        intial={
            'first_name':data.first_name,
            'last_name':data.last_name,
            'country':data.country,
            'city':data.city,
        }

        form=self.form_class(initial=intial)
        return render(requset,'Accounts/Update_user.html',context={'title':'Update User','form':form,'data':data})

    def post(self,request,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=User.objects.get(id=request.user.id)
            user.last_name=form.cleaned_data['last_name']
            user.first_name=form.cleaned_data['first_name']
            user.country=form.cleaned_data['country']
            user.city=form.cleaned_data['city']
            user.save()
            return HttpResponseRedirect('/')