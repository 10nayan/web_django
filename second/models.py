from django.db import models
import datetime

class Movie(models.Model):
    name=models.CharField(max_length=50)
    release_year=models.CharField(max_length=10)
    director=models.CharField(max_length=50)
    actor=models.CharField(max_length=50)
    def __str__(self):
        return self.name+' '+self.release_year+" "+self.director+' '+self.actor


class User(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    date_created=models.DateTimeField(auto_now=True)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=20)
    birthday=models.DateField()
    age=models.DecimalField(max_digits=3, decimal_places=0)
    CheckedIn=models.BooleanField(null=False,blank=False)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"