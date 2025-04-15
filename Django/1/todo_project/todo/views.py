from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.

def task_list(request):
  tasks = Task.objects.all()
  output = "<h1>To-Do List</h1><ul>"
  for task in tasks:
    output += f"<li>{task.title} (Created At: {task.created_at})</li>"
  output += "</ul>"
  return HttpResponse(output)
