from django.db import models
from django.contrib.auth.models import User

class PlatformUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    GROUP_CHOICES = [
        ('student', 'student'),
        ('teacher', 'teacher')
    ]
    group_choice = models.CharField(max_length=20, choices=GROUP_CHOICES)

class ProjectToCreate(models.Model):
    project_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    teacher = models.CharField(max_length=30)
    _class = models.CharField(max_length=3)
    description = models.TextField(max_length=300, blank = True)
    deadline = models.DateField()

    def __str__(self):
        return self.project_name

class ProjectToUpload(models.Model):
    project_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    project = models.FileField()
    done = models.BooleanField(default=False)

class Student(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)

   class Meta:
       permissions = (
           ("student-site-acces", "Can acces student site"),
       )

   def __str__(self):
      return self.user.username


class Teacher(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)

   class Meta:
       permissions = (
           ("teacher-site-acces", "Can acces teacher site"),
       )

   def __str__(self):
      return self.user.username

class Lesson(models.Model):
    subject = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
       return self.subject
