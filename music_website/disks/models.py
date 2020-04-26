from math import ceil

from django.db import models


class Artist(models.Model):
    Name = models.CharField(max_length=120)

    class Meta:
        db_table = "disks_artist"

    def __str__(self):
        return self.Name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    Title = models.CharField(max_length=160)

    class Meta:
        db_table = "disks_album"

    def __str__(self):
        return self.Title


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Composer = models.CharField(max_length=220)
    Milliseconds = models.TextField()
    Bytes = models.IntegerField()
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "disks_track"

    def __str__(self):
        return self.Name
