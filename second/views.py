from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie,User
from .forms import MovieForm,Task,UserForm
from django.http import HttpResponse
task_name=[]
def home(request):
    return render (request, 'second/navbar.html')

def index(request):
    objs=Movie.objects.all()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/second/home')
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
            form.save()
            return redirect('/second/register')
    else:
        form=UserForm()
    return render(request,'second/register.html',{'form':form})
def movie_details(request,my_id=1):
    #movie=Movie.objects.get(id=my_id)
    movie=get_object_or_404(Movie,id=my_id)
    context={
        "objects":movie
    }
    return render(request,'second/detail.html',context)
def movie_delete(request,my_id=1):
    movie=Movie.objects.get(id=my_id)
    context={
        "objects":movie
    }
    if request.method=="POST":
        movie.delete()
        return redirect('../../')
    return render (request,'second/delete.html',context)
# Create your views here.
