# Generated by Django 5.0 on 2023-12-20 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fee_app', '0002_vehicle_parking_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_num',
            field=models.CharField(max_length=20),
        ),
    ]