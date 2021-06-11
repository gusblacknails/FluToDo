from django.contrib import admin
from .models import Task
# Register your models here.


class TasksAdmin(admin.ModelAdmin):

    list_display = ['task_name', 'is_completed', 'date_of_creation']
    list_filter = ['is_completed']

    class Meta:
        model = Task


admin.site.register(Task, TasksAdmin)
