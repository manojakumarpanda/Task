#from django.forms import Form
from django import forms
from .models import User
from django.contrib import messages


class User_form(forms.Form):
    email       =forms.CharField(max_length=50, label='email', widget=forms.EmailInput(
        attrs={
            'placeholder':'Youremail@emali.com'
                        }
                    ))
    first_name  = forms.CharField(max_length=50, label='first_name', widget=forms.TextInput(
        attrs={
            'placeholder':'Enter first_name'
                        }
                    ))
    last_name   = forms.CharField(max_length=50, label='last_name', widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter last_name'
                        }
                    ))

    country     =forms.CharField(max_length=50, label='country', widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your country'
                        }
                    ))
    city        = forms.CharField(max_length=50, label='city', widget=forms.TextInput(
        attrs={
            'placeholder':'Enter city'
                        }
                    ))
    username = forms.CharField(max_length=50, label='username', widget=forms.TextInput(
        attrs={
            'placeholder': ' Enter your username'
        }
    ))
    password = forms.CharField(max_length=50,
                               label='password',
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': ' Enter password Here'}
                               )

                               )

    def clean(self):
        get_data    =super().clean()
        username    =get_data['username']
        email       =get_data['email']

        if username:
            exist=User.objects.filter(username__iexact=username).exists()

            if exist:
                raise forms.ValidationError('The usernmae is already taken')

            elif User.objects.filter(email__iexact=email).exists():
                raise forms.ValidationError('This email is already taken')


    class Meta:
        models='User'
        fields='__all__'

class User_login(forms.Form):
    username = forms.CharField(max_length=50, label='username', widget=forms.TextInput(
        attrs={
            'placeholder': ' Username/email '
        }
    ))
    password = forms.CharField(max_length=50,
                               label='password',
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': ' Enter password Here'}
                               )

                               )

class User_Update_form(forms.Form):
    first_name  = forms.EmailField(
                    widget=forms.TextInput(
                        attrs={
                            'plceholder':'Enter first_name'
                        }
                    ))
    last_name   = forms.EmailField(
                    widget=forms.TextInput(
                        attrs={
                            'plceholder':'Enter last_name'
                        }
                    ))

    country     = forms.EmailField(
                    widget=forms.TextInput(
                        attrs={
                            'plceholder':'Enter your country'
                        }
                    ))
    city        = forms.EmailField(
                    widget=forms.TextInput(
                        attrs={
                            'plceholder':'Enter city'
                        }
                    ))
    username = forms.CharField(max_length=50, label='username', widget=forms.TextInput(
        attrs={
            'placeholder': ' Enter your username'
        }
    ))

    class Meta:
        models='User'
        fields=['first_name','last_name','country','city']