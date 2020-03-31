from django.shortcuts import render
from django.http import HttpResponse

from home.models import Setting


def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'index.html', context)

# Create your views here.


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def blog_single(request):
    return render(request, 'blog-single.html')


def contact(request):
    return render(request, 'contact.html')


def faq(request):
    return render(request, 'faq.html')


def gallery(request):
    return render(request, 'gallery.html')


def job_listings(request):
    return render(request, 'job-listings.html')


def job_single(request):
    return render(request, 'job-single.html')


def login(request):
    return render(request, 'login.html')


def main(request):
    return render(request, 'main.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def portfolio_single(request):
    return render(request, 'portfolio-single.html')


def post_job(request):
    return render(request, 'post-job.html')


def service_single(request):
    return render(request, 'service-single.html')


def services(request):
    return render(request, 'services.html')


def testimonials(request):
    return render(request, 'testimonials.html')

