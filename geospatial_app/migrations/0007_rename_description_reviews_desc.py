# Generated by Django 4.2.5 on 2023-09-20 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geospatial_app', '0006_reviews_trustedby'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='description',
            new_name='desc',
        ),
    ]