# Generated by Django 3.0.3 on 2020-05-25 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isIlan', '0016_ilan_yayintarihi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilan',
            name='personelSayisi',
            field=models.CharField(default='Belirtilmemiştir', max_length=16),
        ),
    ]