from django.urls import path
from . import views 


urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout_view/', views.logout_view, name='logout_view')
]
