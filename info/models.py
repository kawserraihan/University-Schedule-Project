import re
from django import forms
from django.db import models
import math
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from datetime import timedelta

from django.forms import ValidationError




# Create your models here.
sex_choice = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

time_slots = (
    ('7:30 - 8:30', '7:30 - 8:30'),
    ('8:30 - 9:30', '8:30 - 9:30'),
    ('9:30 - 10:30', '9:30 - 10:30'),
    ('11:00 - 11:50', '11:00 - 11:50'),
    ('11:50 - 12:40', '11:50 - 12:40'),
    ('12:40 - 1:30', '12:40 - 1:30'),
    ('2:30 - 3:30', '2:30 - 3:30'),
    ('3:30 - 4:30', '3:30 - 4:30'),
    ('4:30 - 5:30', '4:30 - 5:30'),
)

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)

test_name = (
    ('Internal test 1', 'Internal test 1'),
    ('Internal test 2', 'Internal test 2'),
    ('Internal test 3', 'Internal test 3'),
    ('Event 1', 'Event 1'),
    ('Event 2', 'Event 2'),
    ('Semester End Exam', 'Semester End Exam'),
)


class User(AbstractUser):

    @property
    def is_teacher(self):
        if hasattr(self, 'teacher'):
            return True
        return False


class Dept(models.Model):
    
    name = models.CharField(max_length=200, default = "CSE")
    
    

    def __str__(self):
        return self.name
    
        

class Batch(models.Model):
    
    name = models.CharField(max_length=200, default="50")
    department = models.ForeignKey(Dept, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


class Section(models.Model):
    
    name = models.CharField(max_length=200, default="A")
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    department = models.ForeignKey(Dept, on_delete=models.CASCADE, editable=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.department:
            self.department = self.batch.department
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.name
    



class ClassDetails(models.Model):
    department = models.ForeignKey(Dept, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    classCode = models.CharField(max_length=200, default=None)  # Change "name" to "classCode"
    day = models.CharField(max_length=200, default=None)
    classSubject = models.CharField(max_length=200, default=None)
    classRoom = models.CharField(max_length=200, default=None)
    classStart = models.CharField(max_length=5, default=None)  # Store as 'HH:MM'
    classEnd = models.CharField(max_length=5, default=None)
    teacherInit = models.CharField(max_length=50, default=None)
    

    def __str__(self):
        return self.classCode
    
    """
    def clean_classStart(self):
        classStart = self.cleaned_data.get('classStart')
        if not re.match(r'^\d{2}:\d{2}$', classStart):
            raise forms.ValidationError("Class Start should be in 'HH:MM' format.")
        return classStart
    
    def clean_classEnd(self):
        classEnd = self.cleaned_data.get('classEnd')
        if not re.match(r'^\d{2}:\d{2}$', classEnd):
            raise forms.ValidationError("Class End should be in 'HH:MM' format.")
        return classEnd

    
    def save(self, *args, **kwargs):
        self.clean_classStart(self.classStart)
        self.clean_classEnd(self.classEnd)
        super().save(*args, **kwargs)

"""
class BusDay(models.Model):
    
    day= models.CharField(max_length=10)

    def __str__(self):
        return self.day

class Route(models.Model):
    route_type = models.CharField(max_length=100)

    def __str__(self):
        return self.route_type   
    

class BusSchedule(models.Model):
    day = models.ForeignKey(BusDay, on_delete=models.CASCADE)
    route_type = models.ForeignKey(Route, on_delete=models.CASCADE, null=True, blank=True)
    time_of_day = models.CharField(max_length=5, default=None)
    bus_number = models.CharField(max_length=10)
    route_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.day} - {self.route_type}"


        
class Course(models.Model):
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    id = models.CharField(primary_key='True', max_length=50)
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=50, default='X')

    def __str__(self):
        return self.name


class Class(models.Model):
    # courses = models.ManyToManyField(Course, default=1)
    id = models.CharField(primary_key='True', max_length=100)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    section = models.CharField(max_length=100)
    sem = models.IntegerField()

    class Meta:
        verbose_name_plural = 'classes'

    def __str__(self):
        d = Dept.objects.get(name=self.dept)
        return '%s : %d %s' % (d.name, self.sem, self.section)



class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id = models.CharField(primary_key=True, max_length=100)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=50, choices=sex_choice, default='Male')
    DOB = models.DateField(default='1980-01-01')

    @staticmethod
    def get_total_teachers():
        return Teacher.objects.count()
    def __str__(self):
        return self.name


# Triggers


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


days = {
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
}






