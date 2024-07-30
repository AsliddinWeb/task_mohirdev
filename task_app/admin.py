from django.contrib import admin
from .models import Project, Task, Comment

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'assigned_to', 'is_completed', 'created_at', 'updated_at')
    search_fields = ('name', 'project__name', 'assigned_to__username')
    list_filter = ('is_completed', 'created_at', 'updated_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'text', 'created_at', 'updated_at')
    search_fields = ('text', 'task__name', 'user__username')
    list_filter = ('created_at', 'updated_at')
