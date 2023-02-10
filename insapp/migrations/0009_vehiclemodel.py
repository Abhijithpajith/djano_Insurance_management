# Generated by Django 4.1.4 on 2023-01-06 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insapp', '0008_delete_vehiclemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=50)),
                ('policy', models.CharField(max_length=40)),
                ('vehicle', models.CharField(max_length=25)),
                ('reg', models.CharField(max_length=25)),
                ('date', models.DateField()),
            ],
        ),
    ]
