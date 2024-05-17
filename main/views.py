from django.shortcuts import render
from .models import Photo
from .models import Review
from .models import Service

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    return render(request, 'main/index.html', {'reviews': reviews})

def about(request):
    photos = Photo.objects.all()
    return render(request, 'main/about.html', {'photos': photos})

def uslugi(request):
    services = Service.objects.all()
    return render(request, 'main/uslugi.html', {'services': services})

def contacts(request):
    return render(request, 'main/contacts.html')

def service_detail_view(request, id):
    service = Service.objects.get(pk=id)
    return render(request, 'main/service_detail.html', {'service': service})

# views.py
from django.shortcuts import render, redirect
from .forms import ApplicationForm

def application_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ApplicationForm()
    return render(request, 'main/uslugi.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')
