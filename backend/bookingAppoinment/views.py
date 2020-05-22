from .models import BookingSlots
from .serializers import UserSerializer, BookingSlotsSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post']


class BookingSlotViewSet(viewsets.ModelViewSet):
    queryset = BookingSlots.objects.all()
    serializer_class = BookingSlotsSerializer
    http_method_names = ['get', 'post', 'patch']
    permission_classes = [permissions.IsAuthenticated]

