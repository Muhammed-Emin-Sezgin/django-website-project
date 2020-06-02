from django.contrib import admin

# Register your models here.
from home.models import Setting, UserProfile, FAQ

from home.models import Setting, ContactFormMessage


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['fname', 'email', 'subject', 'message', 'status', 'ip', 'note']
    list_filter = ['status']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'username', 'email', 'first_name',
                    'last_name', 'phone', 'city', 'country', 'last_login']


class faqAdmin(admin.ModelAdmin):
    list_display = ['no', 'question', 'answer', 'status']
    list_filter = ['status']


admin.site.register(ContactFormMessage, ContactFormMessageAdmin)
admin.site.register(Setting)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(FAQ, faqAdmin)
