from django.shortcuts import render
from django.views import generic
from .models import Table, Reservation

# Create your views here.

def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def location(request):
    return render(request, 'location.html')