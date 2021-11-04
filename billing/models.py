
from django.db import models
from django.contrib.auth.models import User

class Billing(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)
    amount = models.DecimalField(max_digits=5,decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
