from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    name = 'chlen'

    return render(request, 'home.html', {'name': name})


def about(request):
    name = 'about us'

    return render(request, 'about.html', {'name': name})