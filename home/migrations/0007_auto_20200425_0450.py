# Generated by Django 3.0.3 on 2020-04-25 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200425_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='calisanSayisi',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='setting',
            name='ofisSayisi',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='setting',
            name='ozgecmisSayisi',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='setting',
            name='uyeSirketSayisi',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]