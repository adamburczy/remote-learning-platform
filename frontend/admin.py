from django.contrib import admin
from .models import Teacher, Student, PlatformUser

class TeacherAdmin(admin.ModelAdmin):
    pass
admin.site.register(Teacher, TeacherAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(PlatformUser, UserAdmin)
