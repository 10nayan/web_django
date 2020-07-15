from django.urls import path
from .views import index,task,register,home,movie_details,movie_delete
app_name='second'
urlpatterns=[
    path("",home,name='home'),
    path("home",index,name="index"),
    path('task', task, name='task'),
    path('register',register, name='register'),
    path('detail',movie_details, name='movie'),
    path('detail/<int:my_id>/',movie_details,name='detail'),
    path('detail/<int:my_id>/delete',movie_delete,name='delete')
]