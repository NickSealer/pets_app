from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('dashboard/', views.dashboard, name='dashboard')
]