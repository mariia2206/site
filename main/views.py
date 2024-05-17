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

from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from .forms import ServiceSignupForm

def service_view(request, id=None):
    if id:
        service = get_object_or_404(Service, id=id)
        if request.method == 'POST':
            form = ServiceSignupForm(request.POST)
            if form.is_valid():
                # Обработка данных формы
                # Например, можно сохранить данные в базу или отправить email
                return redirect('main/uslugi.html', id=id)

    else:
        services = Service.objects.all()
        return render(request, 'main/uslugi.html', {'services': services})
