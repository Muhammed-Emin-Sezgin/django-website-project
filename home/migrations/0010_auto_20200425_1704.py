# Generated by Django 3.0.3 on 2020-04-25 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200425_0526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactformmessage',
            old_name='name',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='contactformmessage',
            old_name='surname',
            new_name='lname',
        ),
    ]
