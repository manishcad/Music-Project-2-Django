from django.db import models

# Create your models here.


class Artist(models.Model):
    artist_name = models.CharField(max_length=100)

    def __str__(self):
        return self.artist_name


class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    date = models.DateTimeField()
    image = models.ImageField()
    des = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Songs(models.Model):
    song_name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_link = models.CharField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.song_name
