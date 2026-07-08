from django.shortcuts import render, redirect 
from .models import Project 
from django.contrib import messages
from .models import ContactMessage

def home_view(request):
    all_projects = Project.objects.all()
    return render(request, 'index.html', {'projects': all_projects})

def contact_view(path_request):
    if path_request.method == 'POST':
        user_email = path_request.POST.get('email')
        user_message = path_request.POST.get('message')
    
        ContactMessage.objects.create(email=user_email, message=user_message)
        
        messages.success(path_request, "Mission log launched successfully!")
        return redirect('home')  
        
    return render(path_request, 'index.html')