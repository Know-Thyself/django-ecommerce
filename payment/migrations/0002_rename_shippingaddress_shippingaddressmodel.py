# Generated by Django 4.2.4 on 2023-09-07 10:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShippingAddress',
            new_name='ShippingAddressModel',
        ),
    ]
