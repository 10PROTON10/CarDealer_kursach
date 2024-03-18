# Generated by Django 3.2.9 on 2023-11-30 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0004_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='contact_information',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='contact_phone',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='O', max_length=1),
        ),
        migrations.AddField(
            model_name='customer',
            name='registration_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]