
from django.shortcuts import render

def Landing(request):
    return render(request, 'home/landing.html')

def Home(request):
    return render(request, 'home/home.html')
