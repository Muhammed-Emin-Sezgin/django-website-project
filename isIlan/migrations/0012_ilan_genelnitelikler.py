# Generated by Django 3.0.3 on 2020-05-25 13:55

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('isIlan', '0011_ilan_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='ilan',
            name='genelNitelikler',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='default'),
        ),
    ]
