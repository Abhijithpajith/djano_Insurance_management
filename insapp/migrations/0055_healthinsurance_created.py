# Generated by Django 4.1.4 on 2023-01-22 20:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('insapp', '0054_alter_vehiclemodel_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthinsurance',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
