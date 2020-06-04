# Register your models here.
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from isIlan.models import Category, Ilan


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent', 'kategoriIsmi']
    list_filter = ['kategoriIsmi']


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "kategoriIsmi"
    list_display = ('tree_actions', 'indented_title', 'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('kategoriIsmi',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Ilan,
                'isTuru',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Ilan,
                 'isTuru',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


class IlanAdmin(admin.ModelAdmin):
    list_display = ['ilanBaslik', 'sirketIsmi', 'user', 'status', 'isTuru']
    list_filter = ['status', 'user', 'sirketIsmi']
    prepopulated_fields = {'slug': ('ilanBaslik',)}


admin.site.register(Category, CategoryAdmin2)
admin.site.register(Ilan, IlanAdmin)
