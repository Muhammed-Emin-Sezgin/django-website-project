"""isBul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('isIlan', include('isIlan.urls')),
    path('home/', include('home.urls')),
    path('product/', include('product.urls')),
    path('user/', include('user.urls')),
    path('favorites/', include('favorites.urls')),
    path('', include('home.urls')),
    path(r'ckeditor/', include('ckeditor_uploader.urls')),
    path('search/', views.ilan_search, name='ilan_search'),
    path(r'search_auto/', views.ilan_search_auto, name='ilan_search_auto'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('job_detail/<slug:slug>/<int:id>', views.job_detail, name='job_detail'),
    path('faq/', views.FAQ, name='faq'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
