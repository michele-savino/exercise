from django.shortcuts import render, get_object_or_404

from .models import Album, Artist, Track
from .forms import SearchForm, NewAlbumForm


def album_list(request):
    albums = Album.objects.order_by('Title')

    return render(request, 'disks/album_list.html', locals())


def album_show(request, id):
    album = get_object_or_404(Album, id=id)
    tracks = album.track_set.all()

    return render(request, 'disks/album.html', locals())


def research(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        what = form.cleaned_data['what']
        albums = Album.objects.filter(Title__contains=query)
        tracks = Track.objects.filter(Name__contains=query)
        artists = Artist.objects.filter(Name__contains=query)

    return render(request, 'disks/search_results.html', locals())


def new_album(request):
    saved = False
    form = NewAlbumForm(request.POST or None)
    if form.is_valid():
        form.save()
        saved = True

    return render(request, 'disks/new_album.html', {
            'form': form,
            'saved': saved
        })