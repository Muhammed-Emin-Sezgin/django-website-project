from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from home.models import Setting
from user.forms import UserUpdateForm, ProfileUpdateForm


def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'user-profile.html', context)


@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profiliniz Başarıyla Güncellendi")
            return redirect('/user')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user-update.html', context)


def user_password(request):
    return HttpResponse("Password")