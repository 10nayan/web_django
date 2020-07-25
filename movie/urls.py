from django.urls import path
from .views import IndexView,MovieListView,MovieDetailView,genrelist_view
urlpatterns=[
    path('', IndexView.as_view(),name='index'),
    path('list', MovieListView.as_view(),name='list'),
    path('<int:pk>/detail',MovieDetailView.as_view(),name='detail'),
    path('list/<str:genre>',genrelist_view,name='genre')
]