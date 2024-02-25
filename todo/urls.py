from django.urls import path
from . import views 
from todo.views import TodosListView


urlpatterns = [
    path('todos/', TodosListView.as_view(), name='index'),
    path('todos/search/', views.search, name='search'),
    path('todos/<int:id>', views.completed, name='completed'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete')
]
