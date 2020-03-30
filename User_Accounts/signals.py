from django.dispatch import receiver
from django.utils.timezone import datetime
from django.contrib.auth import user_logged_in,user_logged_out
from .models import User,Log_Activity
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.shortcuts import redirect


@receiver(user_logged_in)
def Create_activity(sender,request,*args,**kwargs):
    activity=Log_Activity.objects.create(user=kwargs['user'],start_time=datetime.now(),session_key=request.session.session_key)




@receiver(user_logged_out)
def destroy_activity(sender,request,*args,**kwargs):
    print(request.session.session_key)
    update=Log_Activity.objects.filter(session_key=request.session.session_key).update(end_time=datetime.now())

    log_out=Session.objects.filter(session_key=request.session.session_key).update(expire_date=datetime.now())
    try:
        session=Session.objects.get(session_key=request.session.session_key)
        session.delete()
    except Session.DoesNotExist:
        #messages.ERROR(request,'Youare not allowed this first login to access this')
        return redirect('accounts/login/')
