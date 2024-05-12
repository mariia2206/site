from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Путь дла страницы главная
    path('about/', views.about, name='about'), # Путь для страницы о нас
    path('uslugi/', views.uslugi, name='uslugi'), # Путь для страницы услуги и акции
    path('contacts/', views.contacts, name='contacts'),  # Путь для страницы контакты
    # Другие URL-шаблоны здесь
]

