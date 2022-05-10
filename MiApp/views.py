from django.shortcuts import render
from django import http

# Create your views here.

def inicio(request):
    return render(request, 'MiApp/father.html')