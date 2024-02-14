from django.shortcuts import render, redirect, HttpResponse
from .forms import SignupForm, SigninForm
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login


# Create your views here.

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == 'GET':
        signup_form = SignupForm()
        return render(request, 'todo/signup.html', {'signup_form': signup_form})
    else:
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
        return redirect(reverse('index'))


@require_http_methods(["GET", "POST"])
def signin(request):
    if request.method == 'GET':
        signin_form = SigninForm()
        return render(request, 'todo/signin.html', {'signin_form': signin_form})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('index'))
        else:
            return HttpResponse('Username/password is incorrect or user dont exists')