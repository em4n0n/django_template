from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    return HttpResponse('<h1> Welcome! </h1>')

def index(request):