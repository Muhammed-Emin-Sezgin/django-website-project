from django.contrib import admin

# Register your models here.
from favorites.models import Favorites


class favoritesAdmin(admin.ModelAdmin):
    list_display = ['user', 'jobPublisher', 'jobName']
    list_filter = ['user']


admin.site.register(Favorites, favoritesAdmin)
