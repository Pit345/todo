from django.contrib.auth.models import User
from django import forms

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        help_texts = {'username': None}
        labels = {"email": "Email"}
        widgets = {'password': forms.TextInput()}