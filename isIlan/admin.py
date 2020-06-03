# Register your models here.
from django.contrib import admin

from isIlan.models import Category, Ilan


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent', 'kategoriIsmi']
    list_filter = ['kategoriIsmi']


class IlanAdmin(admin.ModelAdmin):
    list_display = ['ilanBaslik', 'sirketIsmi', 'user', 'status']
    list_filter = ['status', 'user', 'sirketIsmi']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Ilan, IlanAdmin)
