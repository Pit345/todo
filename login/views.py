from django.shortcuts import render, redirect, HttpResponse
from .forms import SignupForm, SigninForm, EditProfileForm
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == 'GET':
        signup_form = SignupForm()
        return render(request, 'todo/signup.html', {'signup_form': signup_form})
    else:
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            username = signup_form.cleaned_data['username']
            email = signup_form.cleaned_data['email']
            password = signup_form.cleaned_data['password']
            User.objects.create_user(username=signup_form.cleaned_data['username'], 
                                     email=signup_form.cleaned_data['email'], 
                                     password=signup_form.cleaned_data['password'])
        return redirect(reverse('index'))
    

@require_http_methods(["GET", "POST"])
def signin(request):
    if request.method == 'GET':
        signin_form = SigninForm()
        return render(request, 'todo/signin.html', {'signin_form': signin_form})
    else:
        user = authenticate(request, username=request.POST['username'], 
                            password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect(reverse('index'))
        else:
            return HttpResponse('Username/password is incorrect or user dont exists')


@require_http_methods(["GET", "POST"])
def edit_profile(request):
    user = request.user

    if request.method == 'GET':
        edit_form = EditProfileForm()
        return render(request, 'todo/edit_form.html', {'edit_form': edit_form})
    else:
        edit_form = EditProfileForm(request.POST)
        if edit_form.is_valid():
            user.username = edit_form.cleaned_data['username']
            user.email = edit_form.cleaned_data['email']
            user.set_password(edit_form.cleaned_data['password'])
            user.save()
        return redirect(reverse('index'))


def logout_view(request):
    messages.info(request, f"User {request.user.username.capitalize()} was log out!")
    logout(request)
    return redirect(reverse('index'))