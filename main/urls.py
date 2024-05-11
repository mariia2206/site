from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Пустой путь для корневого URL-адреса
    path('about/', views.about, name='about'),
    # Другие URL-адреса
]