# Generated by Django 3.0.3 on 2020-03-30 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200330_0405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='images',
            new_name='image',
        ),
    ]
