# Generated by Django 3.0.3 on 2020-06-03 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_auto_20200603_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('Pending', 'Pending'), ('False', 'False')], default='Pending', max_length=10),
        ),
    ]
