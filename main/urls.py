from django.urls import path
from . import views
from .views import uslugi, success_view, submit_form

urlpatterns = [
    path('', views.index, name='index'),  # Путь для страницы главная
    path('about/', views.about, name='about'),  # Путь для страницы о нас
    path('uslugi/', uslugi, name='uslugi'),  # Путь для страницы услуги и акции
    path('submit_form/', submit_form, name='submit_form'),  # Путь для обработки формы
    path('contacts/', views.contacts, name='contacts'),  # Путь для страницы контакты
    path('service/<int:id>/', views.service_detail_view, name='service_detail'),
    path('success/', success_view, name='success_view'),
    path('personal.html/', views.privacy_policy, name='privacy_policy'),
]
