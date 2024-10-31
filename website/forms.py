from .models import Reservation, Table
from django import forms

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_date', 'start_time', 'guests']
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 8}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ReservationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        reservation = super(ReservationForm, self).save(commit=False)
        reservation.user = self.user
        if commit:
            reservation.save()
        return reservation