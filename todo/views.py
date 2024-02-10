from django.shortcuts import render
from .models import Task

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})