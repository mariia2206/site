from django.shortcuts import render
from .models import Photo
from .models import Product
from .forms import SearchForm
from .models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    return render(request, 'main/index.html', {'reviews': reviews})

def about(request):
    photos = Photo.objects.all()
    return render(request, 'main/about.html', {'photos': photos})

def uslugi(request):
    return render(request, 'main/uslugi.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Выполните поиск с использованием query, например:
            results = Product.objects.filter(name__icontains=query)  # Замените на свой запрос
            return render(request, 'main/search_results.html', {'results': results})
    else:
        form = SearchForm()
    return render(request, 'main/search_form.html', {'form': form})

