from django.db import models
import datetime

class Movie(models.Model):
    name=models.CharField(max_length=50)
    release_year=models.CharField(max_length=10)
    director=models.CharField(max_length=50)
    actor=models.CharField(max_length=50)
    def __str__(self):
        return self.name+' '+self.release_year+" "+self.director+' '+self.actor


