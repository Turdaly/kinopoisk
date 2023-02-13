from django import forms
from .models import Movie

class MovieCreationForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'genre', 'country', 'duration', 'description', 'rating', 'manufacturing_date', 'image')
        widgets = {
            'name': forms.TextInput,
            'genre': forms.TextInput,
            'country': forms.TextInput,
            'duration': forms.TextInput,
            'description': forms.TextInput,
            'rating': forms.NumberInput,
            'manufacturing_date': forms.TextInput,
            'image': forms.FileInput
        },
        labels = {
            'name': 'имя',
            'genre': 'жанр',
            'country': 'страна',
            'duration':'длительность',
            'description': 'описания',
            'rating': 'рейтинг',
            'manufacturing_date': 'дата выхода',
            'image': 'изображение',
        }
    
