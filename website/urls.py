from django.urls import include, path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='index'),
    path('menu/', views.menu, name='menu'),
    path('location/', views.location_view, name='location'),
    path('make-reservation/', views.make_reservation, name='make_reservation'),
    path('reservation-success/', views.reservation_success, name='reservation_success'),
    path('manage-reservations/', views.manage_reservations, name='manage_reservations'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='account/password-reset.html'), name='password_reset'),
    path('reservation/<int:reservation_id>/update/', views.update_reservation, name='update_reservation'),
    path('reservation/<int:reservation_id>/delete/', views.delete_reservation, name='delete_reservation'),
    path('profile/', views.profile, name='profile'),
    path("profile/delete-account/", views.delete_account, name="delete_account"),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls'))
    ]