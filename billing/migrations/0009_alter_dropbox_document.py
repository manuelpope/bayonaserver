# Generated by Django 3.2.9 on 2021-11-05 16:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('billing', '0008_dropbox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropbox',
            name='document',
            field=models.FileField(blank=True, max_length=30, null=True, upload_to='',
                                   validators=[django.core.validators.FileExtensionValidator(['pdf', 'jpg', 'csv'])]),
        ),
    ]
