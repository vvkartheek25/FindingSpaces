from rest_framework import routers
from .api import BuyerViewSet

router = routers.DefaultRouter()
router.register('api/buyer',BuyerViewSet,'buyerbackend')

urlpatterns = router.urls