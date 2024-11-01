from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('menu/', views.menu, name='menu'),
    path('location/', views.location, name='location'),
    path('make-reservation/', views.make_reservation, name='make_reservation'),
    path('reservation-success/', views.reservation_success, name='reservation_success'),
    path('manage-reservations/', views.manage_reservations, name='manage_reservations'),
    path('reservation/<int:reservation_id>/update/', views.update_reservation, name='update_reservation'),
    path('reservation/<int:reservation_id>/delete/', views.delete_reservation, name='delete_reservation'),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls'))
    ]