# forms.py
from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'review_text', 'photo']

from .models import Action

class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ['photo2', 'author2']


from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'full_description', 'photo']

# forms.py
from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'phone', 'tire_size', 'service', 'appointment_date', 'appointment_time', 'comment', 'agreement']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }
