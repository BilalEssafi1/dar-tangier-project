from .models import Reservation, Table, TIME_SLOTS
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.core.validators import MaxLengthValidator

# Form to handle reservation creation and editing
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_date', 'reservation_time', 'guests']
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'reservation_date'}),
            'reservation_time': forms.Select(attrs={'class': 'form-control', 'id': 'start_time'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 4, 'id': 'guests'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ReservationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        reservation = super(ReservationForm, self).save(commit=False)
        reservation.user = self.user

        time_mapping = dict(TIME_SLOTS)

        if reservation.reservation_time in time_mapping:
            start_time_str, ent_time_str = time_mapping[reservation.reservation_time].split(' - ')
            reservation.start_time = timezone.datetime.strptime(start_time_str, '%H:%M').time()
            reservation.end_time = timezone.datetime.strptime(ent_time_str, '%H:%M').time()

        if commit:
            reservation.save()
        return reservation

# Form for updating user details like username, first name, lastname and email
class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        max_length=20,
        validators=[MaxLengthValidator(20)],
        required=True 
    )
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

# Form for allowing to change password
class CustomPasswordChangeForm(PasswordChangeForm):
    pass