# Generated by Django 3.0.3 on 2020-06-03 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default=True, max_length=10),
            preserve_default=False,
        ),
    ]
