# Generated by Django 5.1.3 on 2024-11-27 23:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_claim_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customar', to=settings.AUTH_USER_MODEL),
        ),
    ]
