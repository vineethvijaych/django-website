from django.shortcuts import render
from . models import *
# Create your views here.

def home(request):
    d={
        'field':picture.objects.all(),
        'field1':image.objects.all(),
        'field2':image1.objects.all()
    }
    return render(request,'home.html',d)

