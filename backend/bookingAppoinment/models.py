from django.db import models
from django.utils import timezone


class BookingSlots(models.Model):

    """
    This model will store all appointment slots.

    appointment_with : Acts as a reference to Users Table. `on_delete` : this is actually a Delete Rule.
    appointment_slot : This wil tell us the actual slot of the appointment
    appointment_booked_by : This is a reference to Users Table which would tell us the Who booked the appointment.
    created : This is just for Logging Purposes (Not Required | Optional).
    """

    appointment_with = models.ForeignKey('auth.User', related_name='appointment_slot', on_delete=models.CASCADE)
    appointment_booked_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    appointment_slot = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
