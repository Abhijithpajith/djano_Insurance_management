# Generated by Django 4.1.4 on 2023-02-10 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insapp', '0070_healthinsurance_helathpayment_lifeinsurance_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='adminmodel',
        ),
        migrations.DeleteModel(
            name='healthInsurance',
        ),
        migrations.DeleteModel(
            name='helathpayment',
        ),
        migrations.DeleteModel(
            name='lifeInsurance',
        ),
        migrations.DeleteModel(
            name='lifepayment',
        ),
        migrations.DeleteModel(
            name='payment',
        ),
        migrations.DeleteModel(
            name='usermodel',
        ),
        migrations.DeleteModel(
            name='vehicleModel',
        ),
    ]
