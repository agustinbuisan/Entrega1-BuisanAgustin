from django.urls import path
from MiApp import views
from .views import *

urlpatterns = [
    path('inicio', views.inicio, name="inicio"),
    
]
