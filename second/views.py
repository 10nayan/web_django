from django.shortcuts import render
from .models import Movie
from .forms import MovieForm
from django.http import HttpResponse


def index(request):
    if request.method=='POST':
        form=MovieForm(request.POST)
        new_movie=form.save()
        return HttpResponse("Saved")
    else:
        form=MovieForm()
    return render(request,'second/index.html',{'form': form})

# Create your views here.
