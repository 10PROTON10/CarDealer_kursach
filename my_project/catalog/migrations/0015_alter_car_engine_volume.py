# Generated by Django 3.2.9 on 2023-12-13 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20231213_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='engine_volume',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
    ]
