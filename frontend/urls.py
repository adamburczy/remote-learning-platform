from django.urls import path
from .views import welcome, choose_role, teacher_register, student_register, student_pannel, teacher_pannel, all_projects, create_project
from django.contrib.auth import views as auth_views

app_name = 'frontend'

urlpatterns = [
    path('', welcome, name='render_welcome_page'),
    path('choose-role', choose_role, name='choose_role'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('teacher-signup/', teacher_register, name='teacher_signup'),
    path('student-signup/', student_register, name='student_signup'),
    path('student-pannel', student_pannel, name='student_pannel'),
    path('teacher-pannel', teacher_pannel, name='teacher_pannel'),
    path('projects/', all_projects, name='all_projects'),
    path('create-project', create_project, name='create_project')
]