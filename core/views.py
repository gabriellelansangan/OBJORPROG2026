from django.shortcuts import render
from .models import Project 

def home_view(request):
    all_projects = Project.objects.all()
    return render(request, 'index.html', {'projects': all_projects})