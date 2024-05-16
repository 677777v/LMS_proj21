from django.contrib import admin
from .models import BugReport, FeatureRequest

# Класс администратора для модели BugReport
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Main Information',
            {
                'classes': ['wide'],
                'fields': ['title', 'description', 'project', 'task'],
            }
        ),
        (
            'Advanced options',
            {
                'classes': ['collapse', 'wide'],
                'fields': ['status', 'priority', 'created_at', 'updated_at'],
            }
        ),
    ]
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('project', 'task', 'status', 'priority')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    actions = ['change_status_to_new', 'change_status_to_in_progress', 'change_status_to_completed']

    def change_status_to_new(self, request, queryset):
        queryset.update(status='New')
    def change_status_to_in_progress(self, request, queryset):
        queryset.update(status='In_progress')
    def change_status_to_completed(self, request, queryset):
        queryset.update(status='Completed')

# Класс администратора для модели FeatureRequest
@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Main Information',
            {
                'classes': ['wide'],
                'fields': ['title', 'description', 'project', 'task'],
            }
        ),
        (
            'Advanced options',
            {
                'classes': ['collapse', 'wide'],
                'fields': ['status', 'priority', 'created_at', 'updated_at'],
            }
        ),
    ]
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('project', 'task', 'status', 'priority')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')