# forms.py
from django import forms
from django.utils.safestring import mark_safe

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

    # Используем виджет Select для создания раскрывающегося списка
    tire_size = forms.ChoiceField(choices=TIRE_SIZE_CHOICES, label='Выберите размер шин:', initial='', widget=forms.Select(), required=True)


    class Meta:
        model = Application
        fields = ['name', 'email', 'phone', 'tire_size', 'service', 'appointment_date', 'appointment_time', 'comment', 'agreement']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите ФИО:', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите e-mail:', 'required': True}),
            'phone': forms.TextInput(attrs={'placeholder': 'Введите номер телефона:', 'required': True}),
            'tire_size': forms.TextInput(attrs={'placeholder': 'Выберите размер шин:', 'required': True}),
            'service': forms.Select({'required': True}),
            'appointment_date': forms.DateInput(attrs={'type': 'date', 'required': True}),
            'appointment_time': forms.TextInput(attrs={'type': 'time', 'required': True}),
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
            'agreement': mark_safe('Я согласен на обработку <a class="persona" href="/personal.html/" target="_blank">персональных данных</a>'),
        }

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
              'agreement': mark_safe('Я согласен на обработку <a class="persona" href="/personal.html/" target="_blank">персональных данных</a>'),
        }
