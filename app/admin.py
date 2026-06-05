from django.contrib import admin
from .models import Workspace, WorkspaceMember, Profile, Task, FocusSession, PlanItem

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'xp', 'streak', 'last_completion_date', 'theme_preference')
    search_fields = ('user__username', 'user__email')
    list_filter = ('theme_preference',)

@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')
    search_fields = ('name', 'created_by__username')
    list_filter = ('created_at',)

@admin.register(WorkspaceMember)
class WorkspaceMemberAdmin(admin.ModelAdmin):
    list_display = ('workspace', 'user', 'role', 'joined_at')
    search_fields = ('workspace__name', 'user__username')
    list_filter = ('role', 'joined_at')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'workspace', 'duration', 'completed', 'assigned_date', 'completed_at')
    list_filter = ('completed', 'assigned_date', 'workspace')
    search_fields = ('title', 'user__username', 'rules')
    ordering = ('-created_at',)

@admin.register(FocusSession)
class FocusSessionAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'user', 'workspace', 'duration', 'completed_at')
    list_filter = ('completed_at', 'workspace')
    search_fields = ('task_title', 'user__username')

@admin.register(PlanItem)
class PlanItemAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'completed', 'order', 'created_at')
    list_filter = ('completed', 'user')
    search_fields = ('text', 'user__username')
