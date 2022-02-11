from django.db import models
from django.urls import reverse
# Create your models here.

class Movie(models.Model):
    movie_name = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    hero = models.CharField(max_length=30)
    herohin = models.CharField(max_length=30)
    released_date = models.DateField()
    genre = models.CharField(max_length=30)
    language = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('/movies')

class Show(models.Model):

    timings = [('10 AM','Morning show   '),('2 PM','Afternoon show    '),('06 PM','Evening show    '),('10 PM','Night show    ')]

    name = models.CharField(max_length=30)
    age = models.IntegerField()
    movie_name = models.CharField(max_length=30)
    show_time = models.CharField(max_length=50, choices=timings)
    theater = models.CharField(max_length=50)
    seats = models.IntegerField(default=1)
    price = models.IntegerField(default=200)
