from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
]