from django.shortcuts import render, HttpResponse, redirect
from .models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def completed(request, id):
    todo = Todo.objects.get(id=id)
    todo.completed = True
    todo.save()
    return redirect('index')