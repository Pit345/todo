from django.shortcuts import render, HttpResponse, redirect
from todo.models import Todo

# Create your views here.

def index(request):
    todos = request.user.todo_set.all()
    return render(request, 'todo/index.html', {'todos': todos})

def completed(request, id):
    todo = Todo.objects.get(id=id)
    if todo.completed == False:
        todo.completed = True
        todo.save()
        return redirect('index')
    else:
        todo.completed = False
        todo.save()
        return redirect('index')