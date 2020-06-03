# Generated by Django 3.0.3 on 2020-06-02 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='faq',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default='New', max_length=10),
        ),
    ]