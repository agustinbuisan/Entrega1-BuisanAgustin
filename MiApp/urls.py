from django.urls import path
from MiApp import views
from .views import *

urlpatterns = [
    path('inicio', views.inicio, name="inicio"),
    path('students', views.students, name="students"),
    path('students_form', views.students_form, name="students_form"),
    path('subjects_form', views.subjects_form, name="subjects_form"),
    path('exams_form', views.exams_form, name="exams_form"),
    path('teachers_form', views.teachers_form, name="teachers_form"),
    path('search_subject', views.search_subject, name="search_subject"),
    path('search/', views.search, name='search'),
    
]
