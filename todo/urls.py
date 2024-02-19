from django.urls import path
from . import views 


urlpatterns = [
    path('todos/', views.index, name='index'),
    path('todos/<int:id>', views.completed, name='completed')
]
