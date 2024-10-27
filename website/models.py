from django.db import models
from django.contrib.auth.models import User

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
    reservation_time =models.TimeField()
    created_at =models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"Reservation by {self.user.username} for {self.reservation_date} at {self.reservation_time}"
