import json

from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from applications.models import Applications
from favorites.models import Favorites
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactForm, ContactFormMessage, IlanForm, FAQ

# Create your views here.
from isIlan.models import Ilan


def homebase(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'homebase.html', context)


def header(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'header.html', context)


def index(request):
    setting = Setting.objects.get(pk=1)
    setting.highlight_index = "nav-link active"
    sliderdata = Ilan.objects.all()[:5]
    jobs = Ilan.objects.all()[:7]
    sayi = Ilan.objects.count()
    context = {'setting': setting,
               'page': 'home',
               'sliderdata': sliderdata,
               'jobs': jobs,
               'sayi': sayi}
    return render(request, 'index.html', context)


def about(request):
    setting = Setting.objects.get(pk=1)
    setting.highlight_about = "nav-link active"
    context = {'setting': setting}
    return render(request, 'about.html', context)


def blog(request):
    setting = Setting.objects.get(pk=1)
    setting.highlight_blog = "nav-link active"
    context = {'setting': setting}
    return render(request, 'blog.html', context)


def blog_single(request):
    setting = Setting.objects.get(pk=1)
    setting.highlight_blogSingle = "nav-link active"
    context = {'setting': setting}
    return render(request, 'blog-single.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.fname = form.cleaned_data['fname']
            data.lname = form.cleaned_data['lname']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderilmiştir. Teşekkür Ederiz...")
            return HttpResponseRedirect('/contact.html')

    setting = Setting.objects.get(pk=1)
    setting.highlight_contact = "nav-link active"
    form = ContactForm()
    context = {'setting': setting, 'form': form}
    return render(request, 'contact.html', context)


def faq(request):
    setting = Setting.objects.get(pk=1)
    setting.highlight_faq = "nav-link active"
    sss = FAQ.objects.all().order_by('no')
    context = {'setting': setting,
               'sss': sss}
    return render(request, 'faq.html', context)


def gallery(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'gallery.html', context)


def job_listings(request):
    setting = Setting.objects.get(pk=1)
    setting.highlight_jobListings = "nav-link active"
    context = {'setting': setting}
    return render(request, 'job-listings.html', context)


def job_single(request):
    setting = Setting.objects.get(pk=1)
    setting.highlight_jobSingle = "nav-link active"
    sliderdata = Ilan.objects.all()[:5]

    context = {'setting': setting,
               'page': 'home',
               'sliderdata': sliderdata,
               }
    return render(request, 'job-single.html', context)


def main(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'main.html', context)


def portfolio(request):
    setting = Setting.objects.get(pk=1)
    setting.highlight_portfolio = "nav-link active"
    context = {'setting': setting}
    return render(request, 'portfolio.html', context)


def portfolio_single(request):
    setting = Setting.objects.get(pk=1)
    setting.highlight_portfolioSingle = "nav-link active"
    context = {'setting': setting}
    return render(request, 'portfolio-single.html', context)


def post_job(request):
    if request.method == 'POST':
        ilan = IlanForm(request.POST, request.FILES)
        if ilan.is_valid():
            data = Ilan()
            data.genelNitelikler = ilan.cleaned_data['genelNitelikler']
            data.tecrube = ilan.cleaned_data['tecrube']
            data.personelSayisi = ilan.cleaned_data['personelSayisi']
            data.genelNitelikler = ilan.cleaned_data['genelNitelikler']
            data.sonBasvuru = ilan.cleaned_data['sonBasvuru']
            data.sirketPoster = ilan.cleaned_data['sirketPoster']
            data.email = ilan.cleaned_data['email']
            data.ilanBaslik = ilan.cleaned_data['ilanBaslik']
            data.konum = ilan.cleaned_data['konum']
            data.isTuru = ilan.cleaned_data['isTuru']
            data.calismaZamani = ilan.cleaned_data['calismaZamani']
            data.isTanimi = ilan.cleaned_data['isTanimi']
            data.sirketIsmi = ilan.cleaned_data['sirketIsmi']
            data.etiketAlani = ilan.cleaned_data['etiketAlani']
            data.sirketWebsite = ilan.cleaned_data['sirketWebsite']
            data.sirketFacebook = ilan.cleaned_data['sirketFacebook']
            data.sirketTwitter = ilan.cleaned_data['sirketTwitter']
            data.sirketLinkedin = ilan.cleaned_data['sirketLinkedin']
            data.sirketLogo = ilan.cleaned_data['sirketLogo']
            data.save()
            messages.success(request, "İlanınız Başarı İle Kaydedilmiştir...")
            return HttpResponseRedirect('/post-job.html')

    setting = Setting.objects.get(pk=1)
    setting.highlight_postJob = "nav-link active"
    ilan = IlanForm()
    context = {'setting': setting, 'ilan': ilan}
    return render(request, 'post-job.html', context)


def service_single(request):
    setting = Setting.objects.get(pk=1)
    setting.highlight_serviceSingle = "nav-link active"
    context = {'setting': setting}
    return render(request, 'service-single.html', context)


def services(request):
    setting = Setting.objects.get(pk=1)
    setting.highlight_services = "nav-link active"
    context = {'setting': setting}
    return render(request, 'services.html', context)


def testimonials(request):
    setting = Setting.objects.get(pk=1)
    setting.highlight_testimonials = "nav-link active"
    context = {'setting': setting}
    return render(request, 'testimonials.html', context)


def ilan_search(request):
    setting = Setting.objects.get(pk=1)
    if request.method == 'POST':
        search = SearchForm(request.POST)
        if search.is_valid():
            query = search.cleaned_data['query']
            konum = search.cleaned_data['sehir']
            calismaSekli = search.cleaned_data['calismaSekli']
            ilanlar = Ilan.objects.filter(sirketIsmi__icontains=query, calismaZamani__icontains=calismaSekli,
                                          konum__icontains=konum)
            if not ilanlar:
                ilanlar = Ilan.objects.filter(ilanBaslik__icontains=query, calismaZamani__icontains=calismaSekli,
                                              konum__icontains=konum)
            sayi = ilanlar.count()
            context = {
                'setting': setting,
                'ilanlar': ilanlar,
                'sayi': sayi,
            }
            return render(request, 'job-listings.html', context)
    return HttpResponseRedirect('/')


def ilan_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        ilan = Ilan.objects.filter(sirketIsmi__icontains=q)
        if not ilan:
            ilan = Ilan.objects.filter(ilanBaslik__icontains=q)
        results = []
        for rs in ilan:
            ilan_json = {}
            ilan_json = rs.sirketIsmi
            results.append(ilan_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'

    return HttpResponse(data, mimetype)


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.warning(request, "Kullanıcı Adı veya Şifre Hatalı!")
            return HttpResponseRedirect('/login')

    setting = Setting.objects.get(pk=1)
    setting.highlight_login = "nav-link active"
    context = {'setting': setting,
               'signup': SignUpForm()}
    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        signup = SignUpForm(request.POST)
        if signup.is_valid():
            signup.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')

    signup = SignUpForm()
    setting = Setting.objects.get(pk=1)
    setting.highlight_login = "nav-link active"
    context = {'setting': setting,
               'signup': signup}
    return render(request, 'login.html', context)


def job_detail(request, slug, id):
    ilan = Ilan.objects.get(pk=id)
    sliderdata = Ilan.objects.all()[:5]

    if Favorites.objects.filter(job_id=id):
        isFavorite = True
    else:
        isFavorite = False

    if Applications.objects.filter(job_id=id):
        isAppeal = True
    else:
        isAppeal = False

    context = {'slug': slug,
               'ilan': ilan,
               'isFavorite': isFavorite,
               'isAppeal'  : isAppeal,
               'sliderdata': sliderdata}

    return render(request, 'job-single.html', context)
