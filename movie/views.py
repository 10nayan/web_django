from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import Movies
from django.views.generic import CreateView, DetailView,ListView,UpdateView,DeleteView
from django.views import View
from django.urls import reverse
from django.http import HttpResponse
# Create your views here.
class IndexView(View):
    template_name='movie/index.html'
    def get(self,request):
        return render (request,self.template_name,{})
class MovieListView(ListView):
    template_name='movie/list.html'
    queryset=Movies.objects.all()
    paginate_by=8
class MovieDetailView(DetailView):
    template_name='movie/detail.html'
    queryset=Movies.objects.all()
def genrelist_view(request,genre):
    movies_list=Movies.objects.filter(Genre__contains=genre)
    paginator = Paginator(movies_list,8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'movie/genre.html',{'page_obj': page_obj,'genre':genre})
def groupby_list_view(request,groupby_arg):
    movies_list=Movies.objects.all()
    if groupby_arg=='Director':
        director_list=sorted(set([i.Director for i in movies_list]))
       # cmn_dir_list=list(set([i for i in director_list if director_list.count(i)>2]))
        paginator = Paginator(director_list,12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    if groupby_arg=='Year':
        year_list=sorted(set([i.ReleaseYear for i in movies_list]))
        paginator = Paginator(year_list,12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    if groupby_arg=='Language':
        lang_list=list(set([i.Language for i in movies_list]))
        paginator = Paginator(lang_list,12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    if groupby_arg=='Cast':
        cast_list1=[i.Cast_I for i in movies_list]
        cast_list2=[j.Cast_II for j in movies_list]
        cast_list=sorted(set([*cast_list1,*cast_list2]))
        paginator = Paginator(cast_list,12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    return render(request,'movie/groupby.html',{'page_obj': page_obj,'groupby_arg':groupby_arg})
def movie_list_view(request,groupby_arg,arg):
    if groupby_arg=='Director':
        movies_list=Movies.objects.filter(Director=arg)
    if groupby_arg=='Year':
        movies_list=Movies.objects.filter(ReleaseYear=arg)
    if groupby_arg=='Language':
        movies_list=Movies.objects.filter(Language=arg)
    if groupby_arg=='Cast':
        movies_list=Movies.objects.filter(Cast_I=arg)| Movies.objects.filter( Cast_II=arg)
    paginator = Paginator(movies_list,8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'movie/genre.html',{'page_obj': page_obj,'genre':groupby_arg})
def like_this_movie(request,key):
    obj=Movies.objects.get(pk=key)
    obj.Like+=1
    obj.save()
    return redirect('/movie/list')
def dislike_this_movie(request,key):
    obj=Movies.objects.get(pk=key)
    obj.Dislike+=1
    obj.save()
    return redirect('/movie/list')