from django.core.files.storage import FileSystemStorage
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets, parsers
from .models import DropBox
from .serializers import DropBoxSerializer
from .models import Billing
from .serializers import BillingSerializer


class BillingViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    permission_classes = (AllowAny,)




class DropBoxViewset(viewsets.ModelViewSet):
    queryset = DropBox.objects.all()
    serializer_class = DropBoxSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = (AllowAny,)
