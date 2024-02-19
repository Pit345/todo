from django.shortcuts import render, redirect
from todo.models import Todo
from django.contrib.auth.decorators import login_required
from login.forms import TodoForm
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

@login_required
def create(request):
    user = request.user
    if request.method == 'GET':
        todo_form = TodoForm()
        return render(request, 'todo/todo_form.html', {'todo_form': todo_form})
    else:
        user.todo_set.create(title=request.POST['title'])
        return redirect(reverse('index'))

@login_required
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

def delete(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('index')