from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.favorites, name='favorites'),
    path('addtofavorites/<int:id>', views.addtofavorites, name='addtofavorites'),
    path('deletefromfavorites/<int:id>', views.deletefromfavorites, name='deletefromfavorites'),
]