# Generated by Django 4.2.7 on 2023-12-26 16:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location_app', '0004_alter_locations_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='locations',
            unique_together={('Userid', 'Latitude', 'Longitude')},
        ),
    ]
