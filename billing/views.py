from django.http import HttpResponseRedirect
from django.shortcuts import render


from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework.views import APIView
from .models import Billing
from .serializers import BillingSerializer, UploadSerializer


class BillingViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    permission_classes = (AllowAny,)

