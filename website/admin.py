from django.contrib import admin
from .models import Table, Reservation
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Reservation)
class ReservationAdmin(SummernoteModelAdmin):
    list_display = ('user', 'table', 'reservation_date',
                    'start_time', 'end_time', 'is_confirmed', 'created_at')
    search_fields = ('user__username', 'table__table_number',)
    summernote_fields = ('content',)


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity', 'is_active')
    search_fields = ('table_number',)