from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from applications.models import Applications


def index(request):
    return HttpResponseRedirect('/applications.html')


@login_required(login_url='/login')
def addtoapplications(request, id):
    url = request.META.get('HTTP_REFERER')
    checkjob = Applications.objects.filter(job_id=id)
    if checkjob:
        messages.info(request, "İlan'a zaten başvurulmuş!")
        return HttpResponseRedirect(url)

    if id:
        current_user = request.user
        data = Applications()
        data.user_id = current_user.id
        data.job_id = id
        data.save()

        messages.success(request, "İlan'a başarı ile başvurulmuştur.")
        return HttpResponseRedirect(url)

    messages.warning(request, "İlan'a başvurulurken hata oluştu!!!")
    return HttpResponseRedirect(url)


@login_required(login_url='/login')
def deletefromapplications(request, id):
    url = request.META.get('HTTP_REFERER')
    Applications.objects.filter(job_id=id).delete()
    messages.success(request, "İlan listeden silinmiştir.")
    return HttpResponseRedirect(url)


@login_required(login_url='/login')
def applications(request):
    current_user = request.user
    applications = Applications.objects.filter(user_id=current_user.id)
    context = {
        'applications': applications
    }

    return render(request, 'applications.html', context)

