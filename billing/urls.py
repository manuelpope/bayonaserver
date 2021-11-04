from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import BillingViewSet

router = routers.DefaultRouter()
router.register('billing', BillingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
