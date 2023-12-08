from django.db import models

class ArtistByRegion(models.Model):
    country = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    song_count = models.IntegerField()

    # def __str__(self):
    #     return f'{self.artist} in {self.country}'


class ArtistSentiment(models.Model):
    artist = models.CharField(max_length=255)
    PositiveCount = models.IntegerField()
    NeutralCount = models.IntegerField()
    NegativeCount = models.IntegerField()

    # def __str__(self):
    #     return f"{self.artist} - Positive: {self.PositiveCount}, Neutral: {self.NeutralCount}, Negative: {self.NegativeCount}, "

class TimelineSong (models.Model):
    artist = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255)
    TrendCount =  models.IntegerField()
    year =  models.IntegerField()

    # def __str__(self):
    #     return f"{self.title} - TrendCount: {self.TrendCount}, Year: {self.year}"

class TimelineArtist (models.Model): 
    artist = models.CharField(max_length=255, null=True)
    SongCount =  models.IntegerField()
    year =  models.IntegerField()

    # def __str__(self):
    #     return f"{self.artist} - TrendCount: {self.SongCount}, Year: {self.year}"
