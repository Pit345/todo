from django.contrib.auth.models import User
from django import forms

class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    
class SigninForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(min_length=5, widget=forms.PasswordInput())

class EditProfileForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class TodoForm(forms.Form):
    title = forms.CharField()