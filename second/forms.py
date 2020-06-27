from django import forms
from django.forms import ModelForm
from .models import Movie,User
class MovieForm(ModelForm):
    class Meta:
        model=Movie
        fields="__all__"
class Task(forms.Form):
    name=forms.CharField(label='Task',max_length=100)
class UserForm(ModelForm):
    class Meta:
        model=User
        fields="__all__"