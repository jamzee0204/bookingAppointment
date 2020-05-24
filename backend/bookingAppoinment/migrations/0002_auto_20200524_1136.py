# Generated by Django 3.0.6 on 2020-05-24 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookingAppoinment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingslots',
            name='appointment_booked',
        ),
        migrations.AddField(
            model_name='bookingslots',
            name='appointment_booked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
