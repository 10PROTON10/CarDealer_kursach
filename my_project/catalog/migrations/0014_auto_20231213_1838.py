# Generated by Django 3.2.9 on 2023-12-13 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20231213_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='drive',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
