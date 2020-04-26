from django import forms
from .models import Album, Artist


class SearchForm(forms.Form):
    query = forms.CharField(label="", max_length=220, widget=forms.TextInput())
    what = forms.CharField(label="", widget=forms.TextInput())


class NewAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
