from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.

# Model representing a dining table in the restaurant
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"

# Model for handling reservations made by users
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Check if the reservation date is in the past
        if self.reservation_date < timezone.now().date():
            raise ValidationError("Reservation date cannot be in the past.")

    def save(self, *args, **kwargs):
        # Ensure validation is called on save
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reservation by {self.user.username} for {self.reservation_date} at {self.reservation_time}"
