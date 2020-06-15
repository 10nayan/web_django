from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1> This is the first page using django</h1>")
