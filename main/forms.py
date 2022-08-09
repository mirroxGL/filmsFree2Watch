from .models import Film
from django.forms import ModelForm, TextInput

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ["title", "rating", "description", "director", "image_url", "imdb_url", "rezka_url"]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            "rating": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rating'
            }),
            "description": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            "director": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Director'
            }),
            "image_url": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Image'
            }),
            "imdb_url": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'IMDB'
            }),
            "rezka_url": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rezka'
            }),
        }