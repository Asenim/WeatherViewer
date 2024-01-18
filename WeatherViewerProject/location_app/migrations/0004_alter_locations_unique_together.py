# Generated by Django 4.2.7 on 2023-12-26 16:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location_app', '0003_alter_locations_userid'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='locations',
            unique_together={('Name', 'Userid')},
        ),
    ]