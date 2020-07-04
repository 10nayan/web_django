from django.urls import path
from .views import index,task,register,home
urlpatterns=[
    path("",home),
    path("home",index,name="index"),
    path('task', task, name='task'),
    path('register',register, name='register')
]