from django.urls import path
from .views import ArticleListView,ArticleDetailView,ArticleCreateView,ArticleUpdateView,ArticleDeleteView,HomeView
urlpatterns=[
    path('',ArticleListView.as_view(),name='home'),
    path('home',HomeView.as_view(),name='homeview'),
    path('<int:id>',ArticleDetailView.as_view(),name='detail'),
    path('create',ArticleCreateView.as_view(),name='create'),
    path('<int:pk>/update',ArticleUpdateView.as_view(),name='update'),
    path('<int:id>/delete',ArticleDeleteView.as_view(),name='delete')
]