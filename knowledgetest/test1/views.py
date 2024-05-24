from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greet(request,id):
    return HttpResponse("<h1>Hi</h1>"+id)