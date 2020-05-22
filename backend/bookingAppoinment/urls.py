from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BookingSlotViewSet

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')
router.register('bookappointment', BookingSlotViewSet, basename='bookappointment')


urlpatterns = [
    path('', include(router.urls)),
]