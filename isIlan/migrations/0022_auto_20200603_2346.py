# Generated by Django 3.0.3 on 2020-06-03 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('isIlan', '0021_auto_20200603_2341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='level',
            new_name='mptt_level',
        ),
    ]
