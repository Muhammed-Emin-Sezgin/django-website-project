# Generated by Django 3.0.3 on 2020-05-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20200517_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='images/users/default.png', upload_to='images/users/'),
        ),
    ]
