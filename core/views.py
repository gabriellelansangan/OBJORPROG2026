from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, PersonalInformation
from django.contrib import messages
from .models import ContactMessage

def home_view(request):
    info = PersonalInformation.objects.first()
    projects = Project.objects.all()

    context = {
        'info' : info,
        'projects' : projects
    }
    return render(request, 'index.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project' : project})

def contact_view(path_request):
    if path_request.method == 'POST':
        user_email = path_request.POST.get('email')
        user_message = path_request.POST.get('message')
    
        ContactMessage.objects.create(email=user_email, message=user_message)
        
        messages.success(path_request, "Mission log launched successfully!")
        return redirect('home')  
        
    return render(path_request, 'index.html')