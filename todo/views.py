from django.shortcuts import render, redirect, HttpResponse
from todo.models import Todo
from django.contrib.auth.decorators import login_required
from login.forms import TodoForm
from django.urls import reverse
from django.contrib import messages
from .forms import SearchForm
from django.views.generic import ListView

# Create your views here.

class TodosListView(ListView):
    model = Todo
    template_name = 'todo/index.html'
    
def search(request):
    todos = Todo.objects.filter(title__contains=request.GET['query'])
    if todos:
        return render(request, 'todo/todos_search.html', {'todos': todos})
    else: 
        return HttpResponse(f"Nothing found {request.GET['query']}, for your search")

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
def delete(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('index')