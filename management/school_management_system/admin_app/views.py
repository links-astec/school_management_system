from django.shortcuts import render, redirect
from django.contrib.auth import login
from .form import UserRegisterForm, StudentRegisterForm, TutorRegisterForm, ParentRegisterForm
from .models import User, Student, Tutor, Parent,Class, Score, Course

from django.contrib.auth.decorators import login_required, user_passes_test

def home(request):
    return render(request, 'admin_app/home.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = UserRegisterForm()
    return render(request, 'admin_app/register.html', {'user_form': user_form})

def register_student(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        student_form = StudentRegisterForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.is_student = True
            user.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            login(request, user)
            return redirect('student_dashboard')
    else:
        user_form = UserRegisterForm()
        student_form = StudentRegisterForm()
    return render(request, 'admin_app/register_student.html', {'user_form': user_form, 'student_form': student_form})

def register_tutor(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        tutor_form = TutorRegisterForm(request.POST)
        if user_form.is_valid() and tutor_form.is_valid():
            user = user_form.save(commit=False)
            user.is_tutor = True
            user.save()
            tutor = tutor_form.save(commit=False)
            tutor.user = user
            tutor.save()
            login(request, user)
            return redirect('tutor_dashboard')
    else:
        user_form = UserRegisterForm()
        tutor_form = TutorRegisterForm()
    return render(request, 'admin_app/register_tutor.html', {'user_form': user_form, 'tutor_form': tutor_form})

def register_parent(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        parent_form = ParentRegisterForm(request.POST)
        if user_form.is_valid() and parent_form.is_valid():
            user = user_form.save(commit=False)
            user.is_parent = True
            user.save()
            parent = parent_form.save(commit=False)
            parent.user = user
            parent.save()
            login(request, user)
            return redirect('parent_dashbaord')
    else:
        user_form = UserRegisterForm()
        parent_form = ParentRegisterForm()
    return render(request, 'admin_app/register_parent.html', {'user_form': user_form, 'parent_form': parent_form})

def is_superadmin(user):
    return user.is_superuser

def is_tutor(user):
    return user.is_tutor

def is_parent(user):
    return user.is_parent

def is_student(user):
    return user.is_student

@login_required
@user_passes_test(is_superadmin)
def superadmin_dashboard(request):
    tutors = Tutor.objects.all()
    classes = Class.objects.all()
    return render(request, 'admin_app/superadmin_dashboard.html', {'tutors': tutors, 'classes': classes})

@login_required
@user_passes_test(is_student)
def student_dashboard(request):
    scores = Score.objects.filter(student=request.user.student)
    return render(request, 'admin_app/student_dashboard.html', {'scores': scores})


@login_required
@user_passes_test(is_tutor)
def tutor_dashboard(request):
    courses = Course.objects.filter(tutor=request.user.tutor)
    students = Student.objects.filter(classes__in=courses.values_list('classes', flat=True))
    return render(request, 'admin_app/tutor_dashboard.html', {'courses': courses, 'students': students})

@login_required
@user_passes_test(is_parent)
def parent_dashboard(request):
    children = request.user.parent.children.all()
    return render(request, 'admin_app/parent_dashboard.html', {'children': children})

@login_required
@user_passes_test(is_tutor)
def update_student_score(request, student_id, course_id):
    student = Student.objects.get(id=student_id)
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        score_value = request.POST.get('score')
        Score.objects.update_or_create(student=student, course=course, defaults={'score': score_value})
        return redirect('tutor_dashboard')
    return render(request, 'admin_app/update_student_score.html', {'student': student, 'course': course})

@login_required
@user_passes_test(is_parent)
def view_child_report(request, child_id):
    child = Student.objects.get(id=child_id)
    scores = Score.objects.filter(student=child)
    return render(request, 'admin_app/view_child_report.html', {'child': child, 'scores': scores})

@login_required
@user_passes_test(is_parent)
def communicate_with_tutor(request, tutor_id):
    tutor = Tutor.objects.get(id=tutor_id)
    if request.method == 'POST':
        message = request.POST.get('message')
        # Handle sending message to the tutor (implementation depends on how you want to manage messages)
        return redirect('parent_dashboard')
    return render(request, 'admin_app/communicate_with_tutor.html', {'tutor': tutor})
