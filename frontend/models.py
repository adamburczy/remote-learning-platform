from django.db import models
from django.contrib.auth.models import User

class PlatformUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    GROUP_CHOICES = [
        ('student', 'student'),
        ('teacher', 'teacher')
    ]
    group_choice = models.CharField(max_length=20, choices=GROUP_CHOICES)

class Project(models.Model):
    nazwa = models.CharField(max_length=50)
    przedmiot = models.CharField(max_length=50)
    nauczyciel = models.CharField(max_length=4)
    opis = models.TextField(max_length=300, blank = True)
    data = models.DateField()


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
