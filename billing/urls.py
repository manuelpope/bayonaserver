from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .views import BillingViewSet, DropBoxViewset

router = routers.SimpleRouter()
router.register('billing', BillingViewSet)
router.register('dropbox', DropBoxViewset)

urlpatterns = [
    path('', include(router.urls)),
]
