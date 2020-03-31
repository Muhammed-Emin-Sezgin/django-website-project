from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('homebase.html', views.homebase, name='index'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('blog.html', views.blog, name='blog'),
    path('blog-single.html', views.blog_single, name='blog-single'),
    path('contact.html', views.contact, name='contact'),
    path('faq.html', views.faq, name='faq'),
    path('gallery.html', views.gallery, name='gallery'),
    path('job-listings.html', views.job_listings, name='job-listings'),
    path('job-single.html', views.job_single, name='job-single'),
    path('login.html', views.login, name='login'),
    path('main.html', views.main, name='main'),
    path('portfolio.html', views.portfolio, name='portfolio'),
    path('portfolio-single.html', views.portfolio_single, name='portfolio-single'),
    path('post-job.html', views.post_job, name='post-job'),
    path('service-single.html', views.service_single, name='service-single'),
    path('services.html', views.services, name='services'),
    path('testimonials.html', views.testimonials, name='testimonials'),

]