# Generated by Django 3.2.9 on 2023-12-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_alter_car_transmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
