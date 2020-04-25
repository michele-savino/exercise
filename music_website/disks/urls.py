from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.album_list, name='album_list'),
    path('album/<int:id>', views.album_show, name='album'),
    path('search', views.research, name='research')
]
