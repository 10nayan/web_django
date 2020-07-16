from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import Article
from .forms import ArticleForm
# Create your views here.
class ArticleListView(ListView):
    # optional
    model=Article
    template_name='blog/article_list.html'
    queryset=Article.objects.all()
class ArticleDetailView(DetailView):
    #if we use pk in url
    #queryset=Article.objects.all()
    template_name='blog/article_detail.html'


    #if we use id in url
    def get_object(self):
        id_=self.kwargs.get('id')
        return get_object_or_404(Article,id=id_)

class ArticleCreateView(CreateView):
    template_name='blog/article_create.html'
    form_class=ArticleForm
    queryset=Article.objects.all()
    #for returning another page
    # success_url="/"
class ArticleUpdateView(UpdateView):
    template_name='blog/article_create.html'
    form_class=ArticleForm
    queryset=Article.objects.all()
    # we use pk instead of id
    def form_valid(self,form):
        return super().form_valid(form)
class ArticleDeleteView(DeleteView):
    template_name='blog/article_delete.html'
    def get_object(self):
        id_=self.kwargs.get('id')
        return get_object_or_404(Article,id=id_)
#    def get_success_url(self):
#       return reverse('home')
