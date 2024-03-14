from rest_framework import routers

from api.views import UserViewSet, VehicleViewSet, VehicleTypeViewSet, VehicleRecordViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet)
router.register('vehicle', VehicleViewSet)
router.register('vehicle_type', VehicleTypeViewSet)
router.register(r'vehicle_record', VehicleRecordViewSet)

urlpatterns = router.urls
