from django.contrib import admin
from .models import ProjectToCreate, Lesson

class ProjectsAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProjectToCreate, ProjectsAdmin)

class LessonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Lesson, LessonAdmin)
