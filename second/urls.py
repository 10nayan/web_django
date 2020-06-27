from django.urls import path
from .views import index,task,register
urlpatterns=[
    path("",index,name="index"),
    path('task', task, name='task'),
    path('register',register, name='register')
]