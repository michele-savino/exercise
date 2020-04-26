from django import forms
from .models import Album


class SearchForm(forms.Form):
    query = forms.CharField(label="Search", max_length=220, widget=forms.TextInput())
    what = forms.CharField(widget=forms.TextInput())


class NewAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('Title', 'artist')