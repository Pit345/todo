from django.urls import path
from . import views 


urlpatterns = [
    path('tasks/', views.index, name='index'),
    path('tasks/<int:id>', views.completed, name='completed')
]
