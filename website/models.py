from django.db import models
from django.contrib.auth.models import User
import random
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.

# Model representing a dining table in the restaurant
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Ensure only a maximum of 10 tables are available
        if self.is_active and Table.objects.filter(is_active=True).count() >= 10:
            raise ValidationError("Cannot have more than 10 active tabels.")
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"

# Model for handling reservations made by users
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    start_time = models.TimeField(default=None)
    end_time = models.TimeField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    def clean(self):
        # Check if the reservation date is in the past
        if self.reservation_date < timezone.now().date():
            raise ValidationError("Reservation date cannot be in the past.")
        # Ensure reservation is made within business hours (10 AM to 11PM)
        if not (timezone.datetime.strptime('10:00', '%H:%M').time() <= self.start_time <= timezone.datetime.strptime('23:00', '%H:%M').time()):
            raise ValidationError("Reservations must be made between 10 AM and 11PM.")
        # Automatically set end time to be 2 hours after start time
        self.end_time = (timezone.datetime.combine(timezone.now(), self.start_time) + timedelta(hours=2)).time()
        # Check for overlapping reservations on the same table
        overlapping_reservations = Reservation.objects.filter(
            table=self.table,
            reservation_date=self.reservation_date,
            start_time_lt=self.end_time,
            end_time_gt=self.start_time,
        ).exclude(id=self.id)
        if overlapping_reservations.exists():
            raise ValidationError("This table is already reserved for the selected time slot.")
        # Check total capacity limit for the reservation with each table offering a maximum capacity of 4
        total_reservations = Reservation.objects.filter(
            reservation_date=self.reservation_date,
            start_time_lt=self.end_time,
            end_time_gt=self.start_time,
            is_confirmed=True
        ).count()
        if total_reservations * 4 >= 40:
            raise ValidationError("This restaurant has reached its maximum capacity for this time slot.")


    def save(self, *args, **kwargs):
        # Ensure validation is called on save
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reservation by {self.user.username} for {self.reservation_date} from {self.start_time} to {self.end_time}"