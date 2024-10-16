from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):

    def __str__(self):
        return f'{self.name}'

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)])
    active = models.fields.BooleanField(default=True)
    official_webpage = models.fields.URLField(null=True, blank=True)



class Title(models.Model):

    class Type(models.TextChoices):
        DISQUES = 'RECORDS'
        VETEMENTS = 'CLOTHING'
        AFFICHE = 'POSTERS'
        DIVERS = 'MISCELLANEOUS'

    name = models.fields.CharField(default='', max_length=100)
    description = models.fields.CharField(default='', max_length=1000)
    sold = models.fields.BooleanField(default=True)
    year = models.IntegerField(default=10)
    type = models.fields.CharField(choices=Type.choices, max_length=15)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)



