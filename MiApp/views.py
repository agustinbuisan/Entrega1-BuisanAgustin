from django.shortcuts import render
from django import http
from .models import *

from MiApp.forms import *

# Create your views here.

def inicio(request):
    return render(request, 'MiApp/father.html')

def students(request):
    return render(request, 'MiApp/students.html')

def students_form(request):

    if request.method == 'POST':

        miFormulario=Student_form(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            student=Student(name=informacion['name'], surname=informacion['surname'], document=informacion['document'], mail=informacion['mail'], age=informacion['age'], school_year=informacion['school_year'])
            student.save()
            return render(request, 'MiApp/students_form.html')

    else:
        miFormulario=Student_form()
    return render(request, 'MiApp/students_form.html', {'formulario': miFormulario})

def teachers_form(request):

    if request.method == 'POST':

        miFormulario=Teacher_form(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            teacher=Teacher(name=informacion['name'], surname=informacion['surname'], subject=informacion['subject'], mail=informacion['mail'])
            teacher.save()
            return render(request, 'MiApp/teachers_form.html')

    else:
        miFormulario=Teacher_form()
    return render(request, 'MiApp/teachers_form.html', {'formulario': miFormulario})

def subjects_form(request):

    if request.method == 'POST':

        miFormulario=Subject_form(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            subject=Subject(subject_name=informacion['subject_name'], teacher_name=informacion['teacher_name'], teacher_surname=informacion['teacher_surname'], day=informacion['day'], start_time=informacion['start_time'], end_time=informacion['end_time'])
            subject.save()
            return render(request, 'MiApp/subjects_form.html')

    else:
        miFormulario=Subject_form()
    return render(request, 'MiApp/subjects_form.html', {'formulario': miFormulario})

def exams_form(request):

    if request.method == 'POST':

        miFormulario=Exam_form(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            exam=Exam(subject=informacion['subject'], date=informacion['date'], student_name=informacion['student_name'], student_surname=informacion['student_surname'], grade=informacion['grade'])
            exam.save()
            return render(request, 'MiApp/exams_form.html')

    else:
        miFormulario=Student_form()
    return render(request, 'MiApp/exams_form.html', {'formulario': miFormulario}) 


def search_subject(request):
    return render(request, 'MiApp/subject_search.html')

def search(request):
    if request.GET['subject_name']:
        subject=request.GET['subject_name']
        
        teachers=Subject.objects.filter(subject_name=subject)

        return render(request, 'MiApp/subject_results.html', {'subject_name':subject})
    else:
        error="No subject was input!"
        return render(request, 'MiApp/subject_results.html', {'error':error})