# Generated by Django 4.2.16 on 2024-10-31 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_reservation_end_time_reservation_is_confirmed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='guests',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
