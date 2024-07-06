from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student, Tutor, Parent
# this file contains the django forms for registering users namely superadmin, tutor, student and parent

class UserRegisterForm(UserCreationForm): # this is the standard user registration form
    full_name = forms.CharField(max_length=150, required=False, help_text='Optional.')
    class Meta:
        model = User
        fields = ['full_name', 'email', 'password1', 'password2']

class StudentRegisterForm(forms.ModelForm): # this is the standard student registration form
    class Meta:
        model = Student
        fields = []

class TutorRegisterForm(forms.ModelForm): # this one is for registering tutors
    class Meta:
        model = Tutor
        fields = []

class ParentRegisterForm(forms.ModelForm): # this one is for parents
    class Meta:
        model = Parent
        fields = []
