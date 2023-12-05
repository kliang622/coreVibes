from django.db import models

class Marker(models.Model):
    country = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    song_count = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        db_table = 'custom_marker_table'