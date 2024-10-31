import os
from django.shortcuts import render, redirect
from django.views import generic
from .models import Table, Reservation
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    form = ReservationForm(user=request.user)
    return render(request, 'index.html', {'form': form})  

def menu(request):
    return render(request, 'menu.html')

def location(request):
    return render(request, 'location.html')

def location_view(request):
    google_maps_api_key = os.environ.get('GOOGLE_MAPS_API_KEY')
    return render(request, 'location.html', {'google_maps_api_key': google_maps_api_key})

@login_required
def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('reservation_success') 
    else:
        form = ReservationForm()
    
    return render(request, 'make_reservation.html', {'form': form})

def reservation_success(request):
    return render(request, 'account/reservation_success.html') 