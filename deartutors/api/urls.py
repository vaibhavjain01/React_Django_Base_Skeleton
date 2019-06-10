from rest_framework import routers
from .api import TestViewSet

router = routers.DefaultRouter()
router.register('api/test', TestViewSet, 'name_test')

urlpatterns = router.urls