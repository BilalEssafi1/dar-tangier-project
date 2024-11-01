from .models import Reservation, Table, TIME_SLOTS
from django import forms
from django.utils import timezone

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_date', 'reservation_time', 'guests']
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'reservation_time': forms.Select(attrs={'class': 'form-control'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 8}),
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