# Generated by Django 4.1.4 on 2023-01-11 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insapp', '0034_alter_vehiclemodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclemodel',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
