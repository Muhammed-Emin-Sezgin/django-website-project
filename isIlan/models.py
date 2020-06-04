from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    kategoriIsmi = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, unique=True)

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['kategoriIsmi']

    def __str__(self):
        full_path = [self.kategoriIsmi]
        k = self.parent
        while k is not None:
            full_path.append(k.kategoriIsmi)
            k = k.parent
        return ' / '.join(full_path[::-1])

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Ilan(models.Model):

    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    calismaZamaniSecenek = (
        ('Yarı Zamanlı', 'Yarı Zamanlı'),
        ('Tam Zamanlı', 'Tam Zamanlı'),
    )

    konumSecenek = (
        ('Tekirdağ', 'Tekirdağ'),
        ('İstanbul', 'İstanbul'),
        ('Ankara', 'Ankara'),
        ('İzmir', 'İzmir'),
        ('Karabük', 'Karabük'),
    )

    status = models.CharField(max_length=15, choices=STATUS, default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
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
    slug = models.SlugField(blank=True, unique=True)
    sonBasvuru = models.DateField(default="2020-07-25")
    yayinTarihi = models.DateField(auto_now=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sirketIsmi

    def get_absolute_url(self):
        return reverse('ilan_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )

    ilan = models.ForeignKey(Ilan, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(blank=True, max_length=50)
    comment = models.CharField(blank=True, max_length=250)
    status = models.CharField(max_length=15, choices=STATUS, default='new')
    ip = models.CharField(blank=True, max_length=20)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment']


