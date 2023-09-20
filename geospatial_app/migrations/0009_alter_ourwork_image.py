# Generated by Django 4.2.5 on 2023-09-20 20:22

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geospatial_app', '0008_backgroundimage_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourwork',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='ourwork_image'),
        ),
    ]
