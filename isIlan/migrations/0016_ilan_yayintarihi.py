# Generated by Django 3.0.3 on 2020-05-25 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isIlan', '0015_ilan_sonbasvuru'),
    ]

    operations = [
        migrations.AddField(
            model_name='ilan',
            name='yayinTarihi',
            field=models.DateField(auto_now=True),
        ),
    ]