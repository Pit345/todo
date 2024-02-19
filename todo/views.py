from django.shortcuts import render, HttpResponse, redirect
from todo.models import Todo
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})    

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