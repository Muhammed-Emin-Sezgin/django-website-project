from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.


class Setting(models.Model):

    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )

    companyname = models.CharField(blank=True, max_length=20)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    trendingkey1 = models.CharField(blank=True, max_length=25)
    trendingkey2 = models.CharField(blank=True, max_length=25)
    trendingkey3 = models.CharField(blank=True, max_length=25)

    adaysayisi = models.CharField(blank=True, max_length=5)
    paylasilanissayisi = models.CharField(blank=True, max_length=5)
    yerlestirileniscisayisi = models.CharField(blank=True, max_length=5)
    sirketsayisi = models.CharField(blank=True, max_length=5)

    calisanSayisi = models.CharField(blank=True, max_length=5)
    ofisSayisi = models.CharField(blank=True, max_length=5)
    ozgecmisSayisi = models.CharField(blank=True, max_length=20)
    uyeSirketSayisi = models.CharField(blank=True, max_length=10)

    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = RichTextUploadingField()
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=20)
    smtpemail = models.CharField(blank=True, max_length=20)
    smtppassword = models.CharField(blank=True, max_length=10)
    smtpport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    linkedin = models.CharField(blank=True, max_length=50)
    aboutus = models.TextField()
    contact = models.TextField(blank=True)
    references = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    highlight_index = models.CharField(blank=True, max_length=30)
    highlight_about = models.CharField(blank=True, max_length=30)
    highlight_blog = models.CharField(blank=True, max_length=30)
    highlight_blogSingle = models.CharField(blank=True, max_length=30)
    highlight_contact = models.CharField(blank=True, max_length=30)
    highlight_faq = models.CharField(blank=True, max_length=30)
    highlight_gallery = models.CharField(blank=True, max_length=30)
    highlight_jobListings = models.CharField(blank=True, max_length=30)
    highlight_jobSingle = models.CharField(blank=True, max_length=30)
    highlight_portfolio = models.CharField(blank=True, max_length=30)
    highlight_login = models.CharField(blank=True, max_length=30)
    highlight_portfolioSingle = models.CharField(blank=True, max_length=30)
    highlight_postJob = models.CharField(blank=True, max_length=30)
    highlight_serviceSingle = models.CharField(blank=True, max_length=30)
    highlight_services = models.CharField(blank=True, max_length=30)
    highlight_testimonials = models.CharField(blank=True, max_length=30)

    def __str__(self):
        return self.title
