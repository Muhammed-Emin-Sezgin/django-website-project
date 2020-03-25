from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    text = "Hello Django"
    bolum = "Computer Engineering"

    context = {'text': text, 'bolum': bolum}
    return render(request, 'index.html', context)

# Create your views here.
