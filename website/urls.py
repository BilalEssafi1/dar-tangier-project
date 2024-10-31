from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('menu/', views.menu, name='menu'),
    path('location/', views.location, name='location'),
    path('make-reservation/', views.make_reservation, name='make_reservation'),
    path('reservation-success/', views.reservation_success, name='reservation_success'),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls'))
    ]