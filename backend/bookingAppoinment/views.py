from .models import BookingSlots
from .serializers import UserSerializer, BookingSlotsSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post']


class BookingSlotViewSet(viewsets.ModelViewSet):
    queryset = BookingSlots.objects.all()
    serializer_class = BookingSlotsSerializer
    http_method_names = ['get', 'post', 'patch']
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(appointment_booked_by=None)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

