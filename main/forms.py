# forms.py
from django import forms
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
import datetime
from .models import Review
from .models import Service
from .models import Application
from .models import Action
import re
from django.core.exceptions import ValidationError


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'review_text', 'photo']



class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ['photo', 'author']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'full_description', 'photo']


class ApplicationForm(forms.ModelForm):
    # Создаем список вариантов для размеров шин
    TIRE_SIZE_CHOICES = [
        ('', 'Выберите размер шин:'),
        ('R13', 'R13'),
        ('R14', 'R14'),
        ('R15', 'R15'),
        ('R16', 'R16'),
        ('R17', 'R17'),
        ('R18', 'R18'),
        ('R19', 'R19'),
        ('R20', 'R20'),
        ('R21', 'R21'),
        ('R22', 'R22'),
    ]
    # Создаем список вариантов для времени
    TIME_CHOICES = [
        ('', 'Выберите время:'),
        ('09:00', '09:00'),
        ('09:40', '09:40'),
        ('10:20', '10:20'),
        ('11:00', '11:00'),
        ('11:40', '11:40'),
        ('12:20', '12:20'),
        ('13:00', '13:00'),
        ('13:40', '13:40'),
        ('14:20', '14:20'),
        ('15:00', '15:00'),
        ('15:40', '15:40'),
        ('16:20', '16:20'),
        ('17:00', '17:00'),
        ('17:40', '17:40'),
        ('18:20', '18:20'),
        ('19:00', '19:00'),
        ('19:40', '19:40'),
        ('20:20', '20:20'),
        ('21:00', '21:00'),
        ('21:40', '21:40'),
    ]

    # Используем виджет Select для создания раскрывающегося списка
    tire_size = forms.ChoiceField(choices=TIRE_SIZE_CHOICES, label='Выберите размер шин:', initial='', widget=forms.Select(), required=True)
    appointment_time = forms.ChoiceField(choices=TIME_CHOICES, label='Выберите время:', required=True,
                                         widget=forms.Select(attrs={'placeholder': 'Выберите время'}))

    class Meta:
        model = Application
        fields = ['name', 'email', 'phone', 'tire_size', 'service', 'appointment_date', 'appointment_time', 'comment', 'agreement']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите ФИО:', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите e-mail:', 'required': True}),
            'phone': forms.TextInput(attrs={'placeholder': 'Введите номер телефона:', 'required': True}),
            'tire_size': forms.TextInput(attrs={'placeholder': 'Выберите размер шин:', 'required': True}),
            'service': forms.Select({'required': True}),
            'appointment_date': forms.DateInput(attrs={'placeholder': 'Выберите дату:','type': 'date', 'required': True}),
            'appointment_time': forms.Select(attrs={'placeholder': 'Выберите время:','required': True}),
            'comment': forms.Textarea(attrs={'placeholder': 'Комментарий', 'rows': 5}),
            'agreement': forms.CheckboxInput(attrs={'class': 'form-check-input', 'required': True}),
        }
        labels = {
            'name': '',
            'email': '',
            'phone': '',
            'tire_size': '',
            'service': '',
            'appointment_date': '',
            'appointment_time': '',
            'comment': '',
            'agreement': mark_safe('Я согласен(-на) на обработку персональных данных в соответствии с <a class="persona" href="/personal.html/" target="_blank">политикой конфиденциальности</a>'),
        }

    def clean_appointment_time(self):
        appointment_date = self.cleaned_data.get('appointment_date')
        appointment_time = self.cleaned_data.get('appointment_time')
        if appointment_date and appointment_time:
            if Application.objects.filter(appointment_date=appointment_date, appointment_time=appointment_time,
                                          approved=True).exists():
                raise ValidationError("Это время уже занято.")
        return appointment_time

    # Функция для проверки почты
    def clean_email(self):
        email = self.cleaned_data['email']
        if '@' not in email:
            raise ValidationError("Email должен содержать символ '@'.")
        return email

    # Функция для появления надписи выберите услугу вместо ----
    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['service'].empty_label = 'Выберите услугу:'

        # Поле комментария необязательное
        self.fields['comment'].required = False

from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'email', 'phone', 'question_text', 'agreement']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите ФИО:', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите email:', 'required': True}),
            'phone': forms.TextInput(attrs={'placeholder': 'Введите номер телефона:', 'required': True}),
            'question_text': forms.Textarea(attrs={'placeholder': 'Введите ваш вопрос:', 'rows': 5, 'required': True}),
            'agreement': forms.CheckboxInput(attrs={'required': True}),
        }
        labels = {
            'name': '',
            'email': '',
            'phone': '',
            'question_text': '',
            'agreement': mark_safe(
                'Я согласен(-на) на обработку персональных данных в соответствии с <a class="persona" href="/personal.html/" target="_blank">политикой конфиденциальности</a>'),
        }
