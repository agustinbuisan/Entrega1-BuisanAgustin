from audioop import maxpp
from django.db import models
from django.forms import EmailField

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    document = models.IntegerField()
    mail = models.EmailField()
    age = models.IntegerField()
    school_year = models.IntegerField()

    def __str__ (self):
        return f"{self.name} {self.surname}"

class Teacher(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    mail = models.EmailField()

    def __str__ (self):
        return f"{self.name} {self.surname}"

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)
    teacher_name = models.CharField(max_length=30)
    teacher_surname = models.CharField(max_length=30)
    day = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__ (self):
        return f"{self.subject_name}"

class Exam(models.Model):
    subject = models.CharField(max_length=50)
    date = models.DateField()
    student_name = models.CharField(max_length=30)
    student_surname = models.CharField(max_length=30)
    grade = models.IntegerField()

    def __str__ (self):
        return f"{self.student_name} {self.student_surname} {self.subject}"