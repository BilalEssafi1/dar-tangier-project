import os
from django.shortcuts import render, redirect
from django.views import generic
from .models import Table, Reservation
from .forms import ReservationForm, UserUpdateForm, CustomPasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import logout
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

# Create your views here.

def home(request):
    form = ReservationForm(user=request.user)
    return render(request, 'index.html', {'form': form})  

def menu(request):
    return render(request, 'menu.html')

def location(request):
    return render(request, 'location.html')

def location_view(request):
    google_maps_api_key = os.environ.get('GOOGLE_API_KEY')
    return render(request, 'location.html', {'google_maps_api_key': google_maps_api_key})

def custom_404(request,  exception):
    context = {'request_path': request.path,}
    response = render(request, 'account/404.html', context)
    response.status_code = 404
    return response

# Make a reservation
@login_required
def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('reservation_success') 
    else:
        form = ReservationForm()
    
    return render(request, 'account/make-reservation.html', {'form': form})

def reservation_success(request):
    return render(request, 'account/reservation-success.html') 

# Manage reservations
@login_required
def manage_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'account/manage-reservations.html', {'reservations': reservations})

# Update a reservation 
@login_required
def update_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    form = ReservationForm(request.POST or None, instance=reservation, user=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, "Reservation updated successfully!")
        return HttpResponseRedirect(reverse('reservation_success'))
    return render(request, 'account/reservation-update.html', {'form': form})

# Delete a reservation
@login_required
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, "Reservation deleted successfully.")
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'account/reservation-confirm-delete.html', {'reservation': reservation})

# Update User Information
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        
        if user_form.is_valid():
            user_form.save()
            
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, password_form.user) 
            return redirect('profile') 

    else:
        user_form = UserUpdateForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'account/profile.html', {
        'user_form': user_form,
        'password_form': password_form,
    })

# Delete Account
@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        logout(request)
        user.delete() 
        messages.success(request, "Your account has been deleted.")
        return redirect("index") 
    return render(request, "account/confirm-delete-account.html")

# Reset Password
class CustomPasswordResetView(PasswordResetView):
    template_name = 'account/password-reset.html'

