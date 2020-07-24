from django.urls import path
from .views import IndexView,MovieListView,MovieDetailView,ActionListView
urlpatterns=[
    path('', IndexView.as_view(),name='index'),
    path('list', MovieListView.as_view(),name='list'),
    path('<int:pk>/detail',MovieDetailView.as_view(),name='detail'),
    path('list/action',ActionListView.as_view(),name='action')
]