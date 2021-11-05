# Generated by Django 3.2.9 on 2021-11-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('billing', '0007_delete_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='DropBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('document', models.FileField(max_length=30, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Drop Boxes',
            },
        ),
    ]
