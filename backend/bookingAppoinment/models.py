from django.db import models
from django.utils import timezone


class BookingSlots(models.Model):

    """    This model will store all appointment slots    """

    appointment_with = models.ForeignKey('auth.User', related_name='appointment_slot', on_delete=models.CASCADE)
    appointment_slot = models.DateTimeField(default=timezone.now)
    appointment_booked = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
