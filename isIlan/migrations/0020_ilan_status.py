# Generated by Django 3.0.3 on 2020-06-03 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isIlan', '0019_ilan_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ilan',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default=False, max_length=15),
        ),
    ]