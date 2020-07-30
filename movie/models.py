from django.db import models
from django.urls import reverse
# Create your models here.
class Movies(models.Model):
    Director=models.CharField(max_length=30)
    Cast_I=models.CharField(max_length=30)
    Cast_II=models.CharField(max_length=30)
    Name=models.TextField()
    ReleaseYear=models.IntegerField()
    ImdbRating=models.CharField(max_length=2)
    Genre=models.TextField(null=True)
    Language=models.CharField(max_length=20,null=True)
    Like=models.IntegerField()
    Dislike=models.IntegerField()
    def like_this_movie(self):
        self.Like+=1
        self.save()
        return reverse ('list',kwargs={})
    def dislike_this_movie(self):
        self.Dislike+=1
        self.save()
        return reverse ('list',kwargs={})
    def __str__(self):
        return f"{self.Name} {self.ReleaseYear}"
    def show_name(self):
        if len(self.Name)>16:
            return self.Name[:14]+".."
        else:
            return self.Name
    def search_trailler(self):
        search_string=self.Name.replace(' ','+')
        search_string+="+trailler"
        return search_string
