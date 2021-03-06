# Generated by Django 3.0.3 on 2020-05-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isIlan', '0006_auto_20200516_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilan',
            name='calismaZamani',
            field=models.CharField(blank=True, choices=[('Yarı Zamanlı', 'Yarı Zamanlı'), ('Tam Zamanlı', 'Tam Zamanlı')], max_length=150),
        ),
        migrations.AlterField(
            model_name='ilan',
            name='isTuru',
            field=models.CharField(blank=True, choices=[('Muhasebe/Finans', 'Muhasebe/Finans'), ('Yapı/Mimar/İnşaat', 'Yapı/Mimar/İnşaat'), ('Üretim/Endüstriyel Ürünler/Otomotiv', 'Üretim/Endüstriyel Ürünler/Otomotiv'), ('Bilişim/Telekom', 'Bilişim/Telekom'), ('Turizm/Gıda/Hizmet', 'Turizm/Gıda/Hizmet'), ('Staj/Yeni Mezun/Part-Time', 'Staj/Yeni Mezun/Part-Time')], max_length=150),
        ),
        migrations.AlterField(
            model_name='ilan',
            name='konum',
            field=models.CharField(choices=[('Tekirdağ', 'Tekirdağ'), ('İstanbul', 'İstanbul'), ('Ankara', 'Ankara'), ('İzmir', 'İzmir'), ('Karabük', 'Karabük')], max_length=150),
        ),
    ]
