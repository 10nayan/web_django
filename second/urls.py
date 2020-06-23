from django.urls import path
from .views import index,task
urlpatterns=[
    path("",index,name="index"),
    path('task', task, name='task')
]