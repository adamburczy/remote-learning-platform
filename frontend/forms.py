from django import forms
from  .models import ProjectToCreate, ProjectToUpload, Lesson

class UploadProjectForm(forms.ModelForm): #Form zamiast ModelForm
    class Meta:
        model = ProjectToUpload
        fields = ('project_name', 'surname', 'project', 'done')
        widgets = {'done': forms.HiddenInput()}

class CreateProjectForm(forms.ModelForm): 
    class Meta:
        model = ProjectToCreate
        fields = '__all__'

class CreateLessonForm(forms.ModelForm): 
    class Meta:
        model = Lesson
        fields = '__all__'




