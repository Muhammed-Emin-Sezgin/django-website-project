# Generated by Django 3.0.3 on 2020-05-25 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isIlan', '0012_ilan_genelnitelikler'),
    ]

    operations = [
        migrations.AddField(
            model_name='ilan',
            name='tecrube',
            field=models.CharField(default='Tecrübesiz', max_length=50),
        ),
    ]