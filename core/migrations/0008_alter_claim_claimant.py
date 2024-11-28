# Generated by Django 5.1.3 on 2024-11-27 22:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_customerpolicy_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='claimant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to=settings.AUTH_USER_MODEL),
        ),
    ]
