
from django.shortcuts import render
from .models import Settings

def index(request):
    settings = Settings.objects.latest("id")   
    return render(request, 'index.html', {'setting': settings})

def about(request):
    settings = Settings.objects.latest("id")
    return render(request, 'about.html', {'setting': settings})


# Create your views here.
