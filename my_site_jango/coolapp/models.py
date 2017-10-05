from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Film(models.Model):
    name = models.CharField(max_length=128)
    director = models.CharField(max_length=128)
    actor = models.TextField()
    about = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    pub_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey('Users')

    def __str__(self):
        return str(self.id)


class Users(models.Model):
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    patronymic = models.CharField(max_length=64)
    email = models.CharField(null=True, max_length=64)

    def __str__(self):
        return self.firstName


class Comments(models.Model):
    content = models.TextField()
    film_id = models.ForeignKey('Film')


class Weather(models.Model):
    city = models.CharField(max_length=64)
    wind = models.IntegerField()
    temp_min = models.IntegerField()
    temp_max = models.IntegerField()
