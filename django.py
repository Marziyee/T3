django-admin startproject user_project
python manage.py startapp users
from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.welcome),
]

