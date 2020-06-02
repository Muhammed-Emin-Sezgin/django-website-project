from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from favorites.models import Favorites
from isIlan.models import Ilan


def index(request):
    return HttpResponseRedirect('/favorites.html')


@login_required(login_url='/login')
def addtofavorites(request, id):
    url = request.META.get('HTTP_REFERER')
    checkjob = Favorites.objects.filter(job_id=id)
    if checkjob:
        return HttpResponseRedirect('/favorites/deletefromfavorites/' + str(id))

    if id:
        current_user = request.user
        data = Favorites()
        data.user_id = current_user.id
        data.job_id = id
        data.save()

        messages.success(request, "İlan başarı ile kaydedilmiştir.")
        return HttpResponseRedirect(url)

    messages.warning(request, "İlan kaydedilirken hata oluştu!!!")
    return HttpResponseRedirect(url)


@login_required(login_url='/login')
def deletefromfavorites(request, id):
    url = request.META.get('HTTP_REFERER')
    Favorites.objects.filter(job_id=id).delete()
    messages.success(request, "İlan listeden silinmiştir.")
    return HttpResponseRedirect(url)


@login_required(login_url='/login')
def favorites(request):
    current_user = request.user
    favorites = Favorites.objects.filter(user_id=current_user.id)
    context ={
        'favorites': favorites
    }
    return render(request, 'favorites.html', context)
