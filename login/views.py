from django.shortcuts import render, redirect
from .forms import SignupForm
from django.urls import reverse

# Create your views here.

def signup(request):
    if request.method == 'GET':
        signup_form = SignupForm()
        return render(request, 'todo/signup.html', {'signup_form': signup_form})
    else:
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
        return redirect(reverse('index'))


def signin(request):
    if request.method == 'POST':
        request.POST