from django.shortcuts import render
from .models import Photo
from .models import Review
from .models import Service
from .models import Action

def about(request):
    photos = Photo.objects.all()
    return render(request, 'main/about.html', {'photos': photos})


def service_detail_view(request, id):
    service = Service.objects.get(pk=id)
    return render(request, 'main/service_detail.html', {'service': service})

from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import Service

def uslugi(request):
    services = Service.objects.all()
    actions = Action.objects.all()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'Спасибо за вашу заявку',
                'Ваш заявка успешно получена. Мы ответим вам в ближайшее время.',
                'your_email@example.com',  # Отправитель
                [form.cleaned_data['email']],  # Получатель
                fail_silently=False,
            )
            return redirect('success_view')
    else:
        form = ApplicationForm()

    return render(request, 'main/uslugi.html', {'actions': actions, 'services': services, 'form': form})

def success_view(request):
    return render(request, 'main/success.html')


from django.shortcuts import render
from django.core.mail import send_mail
from .forms import QuestionForm

def index(request):
    reviews = Review.objects.all()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'Спасибо за ваш вопрос',
                'Ваш вопрос успешно получен. Мы ответим вам в ближайшее время.',
                'your_email@example.com',  # Отправитель
                [form.cleaned_data['email']],  # Получатель
                fail_silently=False,
            )
            return render(request, 'main/thank_you.html')
    else:
        form = QuestionForm()
    return render(request, 'main/index.html', {'reviews': reviews , 'form': form})


def contacts(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'Спасибо за ваш вопрос',
                'Ваш вопрос успешно получен. Мы ответим вам в ближайшее время.',
                'your_email@example.com',  # Отправитель
                [form.cleaned_data['email']],  # Получатель
                fail_silently=False,
            )
            return render(request, 'main/thank_you.html')
    else:
        form = QuestionForm()
    return render(request, 'main/contacts.html', {'form': form})

def privacy_policy(request):
    return render(request, 'main/personal.html')