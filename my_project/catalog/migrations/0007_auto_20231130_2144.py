# Generated by Django 3.2.9 on 2023-11-30 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]