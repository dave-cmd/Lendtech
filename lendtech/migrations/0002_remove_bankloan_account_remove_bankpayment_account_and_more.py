# Generated by Django 4.0.6 on 2022-07-09 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lendtech', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankloan',
            name='account',
        ),
        migrations.RemoveField(
            model_name='bankpayment',
            name='account',
        ),
        migrations.RemoveField(
            model_name='mobileloan',
            name='account',
        ),
        migrations.RemoveField(
            model_name='mobilepayment',
            name='account',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='account',
        ),
        migrations.AddField(
            model_name='bankloan',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bankpayment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mobileloan',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mobilepayment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
