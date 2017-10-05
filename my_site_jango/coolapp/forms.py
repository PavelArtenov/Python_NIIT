from django import forms
from .models import Film, Comments


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('name', 'director', 'actor', 'about', 'rating', 'user_id')


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('content',)
