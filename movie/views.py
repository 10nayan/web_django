from django.shortcuts import render
from django.core.paginator import Paginator
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
def genrelist_view(request,genre):
    object_list=Movies.objects.filter(Genre__contains=genre)
    paginator = Paginator(object_list,8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'movie/list.html',{'page_obj': page_obj,'object_list':object_list})