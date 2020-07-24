from django.shortcuts import render
from .models import Movies
from django.views.generic import CreateView, DetailView,ListView,UpdateView,DeleteView
from django.views import View
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
class ActionListView(ListView):
    template_name='movie/list.html'
    queryset=Movies.objects.filter(Genre__contains="Action")
    paginate_by=8