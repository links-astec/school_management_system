
from django.contrib.auth.models import AbstractUser #using this class to create custom users
from django.db import models

class User(AbstractUser): # this is the user class
    is_tutor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    full_name = models.CharField(max_length=150, blank=True, null=True)
    def __str__(self):
        return self.username


class Class(models.Model): # this is the students' class python class
    name = models.CharField(max_length=100)
    tutor = models.ForeignKey('Tutor', on_delete=models.SET_NULL, null=True, blank=True)
    students = models.ManyToManyField('Student', related_name='classes')

class Course(models.Model): # this is the course class
    name = models.CharField(max_length=100)
    tutor = models.ForeignKey('Tutor', on_delete=models.SET_NULL, null=True, blank=True)
    classes = models.ManyToManyField('Class', related_name='courses')

class Student(models.Model): # this class is used to create a new student
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parents = models.ManyToManyField('Parent', related_name='children')

class Tutor(models.Model): # this is class is used to create tutors for a particular course
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, related_name='tutors')

class Parent(models.Model): # this is the parent class for adding parents
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Score(models.Model): # this is the score class used by  tutors to update scores for students
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.IntegerField()
