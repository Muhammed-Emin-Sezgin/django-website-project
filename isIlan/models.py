from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.


class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    kategoriIsmi = models.CharField(max_length=50)
    slug =models.SlugField(blank=True)

    def __str__(self):
        return self.kategoriIsmi


class Ilan(models.Model):

    calismaZamaniSecenek = (
        ('Yarı Zamanlı', 'Yarı Zamanlı'),
        ('Tam Zamanlı', 'Tam Zamanlı'),
    )

    isTuruSecenek = (
        ('Muhasebe/Finans', 'Muhasebe/Finans'),
        ('Yapı/Mimar/İnşaat', 'Yapı/Mimar/İnşaat'),
        ('Üretim/Endüstriyel Ürünler/Otomotiv', 'Üretim/Endüstriyel Ürünler/Otomotiv'),
        ('Bilişim/Telekom', 'Bilişim/Telekom'),
        ('Turizm/Gıda/Hizmet', 'Turizm/Gıda/Hizmet'),
        ('Staj/Yeni Mezun/Part-Time', 'Staj/Yeni Mezun/Part-Time'),
    )

    konumSecenek = (
        ('Tekirdağ', 'Tekirdağ'),
        ('İstanbul', 'İstanbul'),
        ('Ankara', 'Ankara'),
        ('İzmir', 'İzmir'),
        ('Karabük', 'Karabük'),
    )

    sirketPoster = models.ImageField(blank=True, upload_to='images/')
    email = models.CharField(max_length=50)
    ilanBaslik = models.CharField(max_length=50)
    konum = models.CharField(max_length=150, choices=konumSecenek)
    isTuru = models.ForeignKey(Category, on_delete=models.CASCADE)
    calismaZamani = models.CharField(max_length=150, choices=calismaZamaniSecenek, blank=True)
    isTanimi = RichTextUploadingField()
    genelNitelikler = RichTextUploadingField(default="default")
    sirketIsmi = models.CharField(max_length=50)
    tecrube = models.CharField(max_length=50, default="Tecrübesiz")
    personelSayisi = models.CharField(max_length=16, default="Belirtilmemiştir")
    etiketAlani = models.CharField(blank=True, max_length=150)
    sirketWebsite = models.CharField(blank=True, max_length=50)
    sirketFacebook = models.CharField(blank=True, max_length=50)
    sirketTwitter = models.CharField(blank=True, max_length=50)
    sirketLinkedin = models.CharField(blank=True, max_length=50)
    sirketLogo = models.ImageField(blank=True, upload_to='images/')
    slug = models.SlugField(blank=True)
    sonBasvuru = models.DateField(default="2020-07-25")
    yayinTarihi = models.DateField(auto_now=True)

    #basvuruBitimi = models.CharField(max_length=50)
    #sorumluluklar = models.CharField(max_length=50)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sirketIsmi

