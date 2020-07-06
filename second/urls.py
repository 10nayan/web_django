from django.urls import path
from .views import index,task,register,home,movie_details
urlpatterns=[
    path("",home),
    path("home",index,name="index"),
    path('task', task, name='task'),
    path('register',register, name='register'),
    path('detail',movie_details, name='movie'),
    path('detail/<int:my_id>',movie_details,name='details')
]