from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.


class Ilan(models.Model):

    calismaZamaniSecenek = (
        ('Part Time', 'Yarı Zamanlı'),
        ('Full Time', 'Tam Zamanlı'),
    )

    isTuruSecenek = (
        ('Part Time', 'Yarı Zamanlı'),
        ('Full Time', 'Tam Zamanlı'),
    )

    sirketPoster = models.ImageField(blank=True, upload_to='images/')
    email = models.CharField(max_length=50)
    ilanBaslik = models.CharField(max_length=50)
    konum = models.CharField(max_length=15)
    isTuru = models.CharField(max_length=10, choices=isTuruSecenek, blank=True)
    calismaZamani = models.CharField(max_length=10, choices=calismaZamaniSecenek, blank=True)
    isTanimi = RichTextUploadingField()
    sirketIsmi = models.CharField(max_length=50)
    etiketAlani = models.CharField(blank=True, max_length=150)
    sirketTanimi = RichTextUploadingField(blank=True)
    sirketWebsite = models.CharField(blank=True, max_length=50)
    sirketFacebook = models.CharField(blank=True, max_length=50)
    sirketTwitter = models.CharField(blank=True, max_length=50)
    sirketLinkedin = models.CharField(blank=True, max_length=50)
    sirketLogo = models.ImageField(blank=True, upload_to='images/')

    #basvuruBitimi = models.CharField(max_length=50)
    #sorumluluklar = models.CharField(max_length=50)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sirketIsmi
