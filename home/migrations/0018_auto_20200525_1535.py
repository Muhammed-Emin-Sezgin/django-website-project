# Generated by Django 3.0.3 on 2020-05-25 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20200525_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='aboutus2Title',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='aboutusTitle',
            field=models.TextField(blank=True),
        ),
    ]
