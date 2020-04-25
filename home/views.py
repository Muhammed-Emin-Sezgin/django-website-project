from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from home.models import Setting, ContactForm, ContactFormMessage


# Create your views here.


def homebase(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'homebase.html', context)


def index(request):
    setting = Setting.objects.get(pk=1)
    setting.highlight_index = "nav-link active"
    context = {'setting': setting}
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
    context = {'setting': setting}
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
    context = {'setting': setting}
    return render(request, 'job-single.html', context)


def login(request):
    setting = Setting.objects.get(pk=1)
    setting.highlight_login = "nav-link active"
    context = {'setting': setting}
    return render(request, 'login.html', context)


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
    setting = Setting.objects.get(pk=1)
    setting.highlight_postJob = "nav-link active"
    context = {'setting': setting}
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
