# Generated by Django 3.2.9 on 2021-11-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('billing', '0003_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='file',
        ),
        migrations.AddField(
            model_name='file',
            name='photo',
            field=models.ImageField(default='blank', upload_to='posts/photos'),
        ),
    ]
