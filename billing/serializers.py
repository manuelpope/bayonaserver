from django.forms import FileField
from rest_framework import serializers

from .models import Billing


class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = ('title', 'description', 'amount','user')
# Serializers define the API representation.
class UploadSerializer(serializers.ModelSerializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']