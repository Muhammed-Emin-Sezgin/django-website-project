from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.applications, name='applications'),
    path('addtoapplications/<int:id>', views.addtoapplications, name='addtoapplications'),
    path('deletefromapplications/<int:id>', views.deletefromapplications, name='deletefromapplications'),
]