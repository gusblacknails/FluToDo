from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Tasks
# Create your views here.

def home_page_view(request):
    return HttpResponse('Hola Hola')


class TasksListView(ListView):
    model = Tasks
    template_name = "templates/todo/tareas_list.html"
    context_object_name = "tasks_list"