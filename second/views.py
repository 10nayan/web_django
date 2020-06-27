from django.shortcuts import render,redirect
from .models import Movie,User
from .forms import MovieForm,Task,UserForm
from django.http import HttpResponse
task_name=[]


def index(request):
    objs=Movie.objects.all()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            new_movie=form.save()
            return redirect('/second/')
    else:
        form=MovieForm()
    return render(request,'second/index.html',{'form': form,'objs':objs})
def task(request):
    if request.method=="POST":
        form=Task(request.POST)
        if form.is_valid():
            tasks=form.cleaned_data['name']
            task_name.append(tasks)
    else:
        form=Task()
    return render(request,'second/task.html',{'form':form,'task_name':task_name})
def register(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            f=form.save()
            return redirect('/second/register')
    else:
        form=UserForm()
    return render(request,'second/register.html',{'form':form})

# Create your views here.
