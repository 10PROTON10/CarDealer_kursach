# Generated by Django 3.2.9 on 2023-12-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_alter_car_transmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel_consumption',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
    ]
