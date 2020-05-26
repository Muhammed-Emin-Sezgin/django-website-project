from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, TextInput, Textarea, ImageField, MultipleChoiceField, FileInput, Select, \
    DateTimeInput

# Create your models here.
from django.utils.safestring import mark_safe

from isIlan.models import Ilan


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
    aboutusTitle = models.TextField(blank=True)
    aboutus = models.TextField(blank=True)
    aboutus2Title = models.TextField(blank=True)
    aboutus2 = models.TextField(blank=True)
    aboutusLink = models.TextField(blank=True)
    aboutusLink2 =models.TextField(blank=True)
    aboutusPicture = models.ImageField(blank=True, upload_to='images/aboutus')
    aboutusPicture2 = models.ImageField(blank=True, upload_to='images/aboutus')
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


class ContactFormMessage(models.Model):

    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
    )

    fname = models.CharField(blank=True, max_length=20)
    lname = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=40)
    subject = models.CharField(blank=True, max_length=50)
    message = models.CharField(blank=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fname


class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['fname', 'lname', 'email', 'subject', 'message']
        widgets = {
        'fname': TextInput(attrs={'class': 'form-control', 'id': 'fname'}),
        'lname': TextInput(attrs={'class': 'form-control', 'id': 'lname'}),
        'email': TextInput(attrs={'class': 'form-control', 'id': 'email'}),
        'subject': TextInput(attrs={'class': 'form-control', 'id': 'subject'}),
        'message': Textarea(attrs={'class': 'form-control', 'id': 'message', 'name': 'message', 'cols': '30', 'rows': '7'})
        }


class IlanForm(ModelForm):
    class Meta:
        model = Ilan
        fields = ['sirketPoster', 'email', 'ilanBaslik', 'konum', 'isTuru', 'calismaZamani', 'isTanimi',
                  'sirketIsmi', 'etiketAlani', 'sirketWebsite', 'sirketFacebook', 'sirketTwitter',
                  'sirketLinkedin', 'sirketLogo', 'sonBasvuru', 'personelSayisi', 'tecrube', 'genelNitelikler']
        widgets = {
            'sirketPoster': FileInput(attrs={'class': 'form-control', 'placeholder': 'Poster'}),
            'email':        TextInput(attrs={'class': 'form-control', 'id': 'email',
                                              'placeholder': 'sirket@domain.com'}),
            'ilanBaslik':   TextInput(attrs={'class': 'form-control', 'id': 'job-title',
                                              'placeholder': 'Örn. Android Developer'}),
            'konum':        Select(attrs={'class': 'selectpicker border rounded', 'data-style': 'btn-black',
                                          'data-width': '100%', 'data-live-search': 'True',
                                          'placeholder': 'Çalışma Zamanı'}, choices=model.konumSecenek),
            'isTuru':       Select(attrs={'class': 'selectpicker border rounded', 'data-style': 'btn-black',
                                          'data-width': '100%', 'data-live-search': 'True', 'placeholder': 'İş Türü'},
                                   choices=model.isTuruSecenek),
            'calismaZamani':Select(attrs={'class': 'selectpicker border rounded', 'data-style': 'btn-black',
                                          'data-width': '100%', 'data-live-search': 'True',
                                          'placeholder': 'Çalışma Zamanı'}, choices=model.calismaZamaniSecenek),
            'isTanimi':     RichTextUploadingField(),
            'genelNitelikler': RichTextUploadingField(),
            'tecrube':      TextInput(attrs={'class': 'form-control', 'id': 'tecrube'}),
            'personelSayisi': TextInput(attrs={'class': 'form-control', 'id': 'personelSayisi'}),
            'sonBasvuru':   DateTimeInput(attrs={'class': 'form-control', 'id': 'sonBasvuru'}),
            'sirketIsmi':   TextInput(attrs={'class': 'form-control', 'id': 'company-name'}),
            'etiketAlani':  TextInput(attrs={'class': 'form-control', 'id': 'company-tagline'}),
            'sirketWebsite':TextInput(attrs={'class': 'form-control', 'id': 'company-website',
                                              'placeholder': 'https://'}),
            'sirketFacebook':TextInput(attrs={'class': 'form-control', 'id': 'company-website-fb',
                                              'placeholder': 'Şirket Facebook Linki'}),
            'sirketTwitter':TextInput(attrs={'class': 'form-control', 'id': 'company-website-tw',
                                              'placeholder': 'Şirket Twitter Linki'}),
            'sirketLinkedin':TextInput(attrs={'class': 'form-control', 'id': 'company-website-tw',
                                              'placeholder': 'Şirket Linkedin Linki'}),
            'sirketLogo':   FileInput(attrs={'class': 'form-control', 'placeholder': 'Logo'})

        }


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=100)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    image = models.ImageField(blank=True, upload_to='images/users/', default='images/users/default.png')

    def __str__(self):
        return self.user.username

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def username(self):
        return self.user.username

    def email(self):
        return self.user.email

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def last_login(self):
        return self.user.last_login


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'city', 'country', 'image']










