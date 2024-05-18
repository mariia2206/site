from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Путь для страницы главная
    path('about/', views.about, name='about'),  # Путь для страницы о нас
    path('uslugi/', views.uslugi, name='uslugi'),  # Путь для страницы услуги и акции
    path('contacts/', views.contacts, name='contacts'),  # Путь для страницы контакты
    path('service/<int:id>/', views.service_detail_view, name='service_detail'),
    path('success/', views.success_view, name='success_view'),

    # Другие URL-шаблоны вашего проекта...
]
