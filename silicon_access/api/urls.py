from django.contrib import admin
from django.urls import path, include

from api import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('users', views.UserViewSet)
router.register('vehicles', views.VehicleViewSet)
router.register('vehicle_types', views.VehicleTypeViewSet)

urlpatterns = router.urls
