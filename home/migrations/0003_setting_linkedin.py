# Generated by Django 3.0.3 on 2020-03-31 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200331_0434'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='linkedin',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
