from django.shortcuts import render, get_object_or_404

from disks.models import Album


def album_list(request):
    albums = Album.objects.order_by('Title')

    return render(request, 'disks/album_list.html', locals())


def album_show(request, id):
    album = get_object_or_404(Album, id=id)
    tracks = album.track_set.all()

    return render(request, 'disks/album.html', locals())
