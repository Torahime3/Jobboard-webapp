from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world ! Index")

def page1(request):
   return HttpResponse("Hello, World ! Page1")

def page2(request):
   return HttpResponse("Hello World ! Page2")
