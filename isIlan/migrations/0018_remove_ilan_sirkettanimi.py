# Generated by Django 3.0.3 on 2020-05-26 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('isIlan', '0017_auto_20200525_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ilan',
            name='sirketTanimi',
        ),
    ]
