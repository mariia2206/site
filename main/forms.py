# forms.py
from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=255)

from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'review_text', 'photo']
