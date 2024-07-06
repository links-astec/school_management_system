from django.contrib import admin

# Register your models here.
# school/admin.py
from django.contrib import admin
from .models import User, Student, Tutor, Parent, Class, Course, Score

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(Parent)
admin.site.register(Class)
admin.site.register(Course)
admin.site.register(Score)
