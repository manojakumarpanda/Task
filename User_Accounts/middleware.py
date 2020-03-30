from django.utils import timezone
from django.contrib.sessions.models import Session
from .models import Log_Activity
from django.contrib import messages

class Account_activity:

    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self, request,*args, **kwargs):

        if request.user.is_authenticated:
            current_session_key=Log_Activity.objects.filter(user__id=request.user.id).first()
            current_session_key=current_session_key.session_key
            if current_session_key and current_session_key!=request.session.session_key:
                try:
                    update=Log_Activity.objects.get(session_key=current_session_key)
                    update.end_time=timezone.datetime.now()
                    update.save()
                except Log_Activity.DoesNotExist:
                    raise messages.ERROR(request,'There is something error try again latter')



        respose=self.get_response(request)
        return respose