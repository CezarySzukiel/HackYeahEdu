from django.contrib import admin
from .models import Homework, HomeworkAssignment, ClassGroup


class HomeworkAssignmentInline(admin.TabularInline):
    model = HomeworkAssignment
    extra = 1


class HomeworkAdmin(admin.ModelAdmin):
    inlines = [HomeworkAssignmentInline]


class ClassGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'homeroom_teacher')


admin.site.register(Homework, HomeworkAdmin)
admin.site.register(ClassGroup, ClassGroupAdmin)
