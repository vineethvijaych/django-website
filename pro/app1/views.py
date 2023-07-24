from django.shortcuts import render
from . models import *
def home(request):
   
    return render(request,'home.html')

def add2(request):
    return render(request,'add2.html')

def view(request):
    d={'fields': pictures.objects.all()}
    return render(request,'add.html',d)
