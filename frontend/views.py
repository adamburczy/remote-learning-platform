from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .forms import UploadProjectForm, CreateProjectForm, CreateLessonForm
from .models import ProjectToCreate, Lesson

def welcome(request):
    return render(request, 'welcome.html')

def choose_role(request):
    return render(request, 'choose_role.html')

def teacher_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.add_message(request, messages.INFO, 'Rejestracja przebiegła pomyślnie.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



def student_register(request):   #thats just basic signup view, without adding to group - if teacher deals with permissions - student dont need to
    if request.method == 'POST':
        form = UserCreationForm(request.POST) ##UserRegistrationForm
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.add_message(request, messages.INFO, 'Your account is registered, you can log in now')
            return redirect('/') #student pannel
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


#@permission_required('projects.teacher-site-acces', login_url='/student-pannel/')
def teacher_pannel(request):
    all_lessons = Lesson.objects.all()
    if request.method =='POST':
        create_lesson = CreateLessonForm(request.POST) 
        if create_project.is_valid:
            print('tu bedzie message')
    else:
        create_lesson = CreateLessonForm()
        #if create_project.is_valid: # message 'zadanie oddano', oddane value = True
        #else: upload_project = UploadProjectForm()
    return render(request, 'teacher_pannel.html', {'form':create_lesson, 'lessons': all_lessons})

def student_pannel(request):
    active_projects = ProjectToCreate.objects.all()
    if request.method =='POST':
        upload_project = UploadProjectForm(request.POST) 
        if upload_project.is_valid: # message 'zadanie oddano', oddane value = True
            print('tu bedzie konfiguracja pliku')
    else:
        upload_project = UploadProjectForm()
    return render(request, 'student_pannel.html', {'form': upload_project, 'active_projects': active_projects})

def all_projects(request):
    projects = ProjectToCreate.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def create_project(request):
    if request.method =='POST':
        create_project = CreateProjectForm(request.POST) 

        if create_project.is_valid:
            print('tu bedzie message')
    else:
        create_project = CreateProjectForm()
        #if create_project.is_valid: # message 'zadanie oddano', oddane value = True
        #else: upload_project = UploadProjectForm()
    return render(request, 'create-project.html', {'form': create_project})





