from .models import BookingSlots
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    This would act as a serializer for Django's Default User-Model.
    Serializer acts as translating JSON-to-medium between our system and outer world.
    """

    class Meta:
        model = User
        fields = '__all__'


class BookingSlotsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingSlots
        fields = '__all__'
