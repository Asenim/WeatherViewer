# Generated by Django 4.2.7 on 2023-11-16 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Latitude', models.DecimalField(decimal_places=5, max_digits=18)),
                ('Longitude', models.DecimalField(decimal_places=5, max_digits=18)),
                ('Userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_app.users')),
            ],
        ),
    ]
