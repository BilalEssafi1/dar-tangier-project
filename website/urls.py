from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('menu/', views.menu, name='menu'),
    path('location/', views.menu, name='location')
    ]