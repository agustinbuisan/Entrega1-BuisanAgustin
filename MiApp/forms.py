from django import forms

class Student_form(forms.Form):
    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    document = forms.IntegerField()
    mail = forms.EmailField()
    age = forms.IntegerField()
    school_year = forms.IntegerField()

class Subject_form(forms.Form):
    subject_name = forms.CharField(max_length=50)
    teacher_name = forms.CharField(max_length=30)
    teacher_surname = forms.CharField(max_length=30)
    day = forms.CharField(max_length=20)
    start_time = forms.TimeField()
    end_time = forms.TimeField()


class Teacher_form(forms.Form):
    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    subject = forms.CharField(max_length=50)
    mail = forms.EmailField()

class Exam_form(forms.Form):
    subject = forms.CharField(max_length=50)
    date = forms.DateField()
    student_name = forms.CharField(max_length=30)
    student_surname = forms.CharField(max_length=30)
    grade = forms.IntegerField()