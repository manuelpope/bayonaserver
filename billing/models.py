from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models


class Billing(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DropBox(models.Model):
    title = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=False,blank=False , default=0)

    document = models.FileField(max_length=30,null=False,
                           blank=True,
                           validators=[FileExtensionValidator( ['pdf','jpg','csv','png'] ) ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'Drop Boxes'
