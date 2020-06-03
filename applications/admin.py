from django.contrib import admin

# Register your models here.
from applications.models import Applications


class applicationsAdmin(admin.ModelAdmin):
    list_display = ['user', 'jobPublisher', 'jobName', 'applicationDate', 'status']
    list_filter = ['user', 'applicationDate', 'status']


admin.site.register(Applications, applicationsAdmin)
