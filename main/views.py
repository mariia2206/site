from django.shortcuts import render
from .models import Photo
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    photos = Photo.objects.all()
    return render(request, 'main/about.html', {'photos': photos})

def uslugi(request):
    return render(request, 'main/uslugi.html')

def contacts(request):
    return render(request, 'main/contacts.html')

