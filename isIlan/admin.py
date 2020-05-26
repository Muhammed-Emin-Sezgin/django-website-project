# Register your models here.
from django.contrib import admin

from isIlan.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent' ,'kategoriIsmi']
    list_filter = ['kategoriIsmi']


admin.site.register(Category, CategoryAdmin)
