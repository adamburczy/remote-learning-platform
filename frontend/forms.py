from django import forms
from .models import Project

class UploadProjectForm(forms.ModelForm): #Form zamiast ModelForm
    class Meta:
        model = Project
        fields = '__all__'

class CreateProjectForm(forms.ModelForm): #Form zamiast ModelForm
    class Meta:
        model = Project
        fields = '__all__'




