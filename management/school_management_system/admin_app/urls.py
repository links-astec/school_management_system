from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('register/student/', views.register_student, name='register_student'),
    path('register/tutor/', views.register_tutor, name='register_tutor'),
    path('register/parent/', views.register_parent, name='register_parent'),
    path('superadmin_dashboard/', views.superadmin_dashboard, name='superadmin_dashboard'),
    path('student_dashboard/', views.student_dashboard,   name = 'student_dashboard'),
    path('tutor_dashboard/', views.tutor_dashboard, name='tutor_dashboard'),
    path('parent_dashboard/', views.parent_dashboard, name='parent_dashboard'),
    path('update_student_score/<int:student_id>/<int:course_id>/', views.update_student_score, name='update_student_score'),
    path('view_child_report/<int:child_id>/', views.view_child_report, name='view_child_report'),
    path('communicate_with_tutor/<int:tutor_id>/', views.communicate_with_tutor, name='communicate_with_tutor'),
    path('login/', auth_views.LoginView.as_view(template_name='admin_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='admin_app/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='admin_app/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='admin_app/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='admin_app/password_reset_complete.html'), name='password_reset_complete'),
]
