from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView
from .models import Project, PersonalInformation, Testimony, Inquiry, ContactMessage
from .forms import ProjectForm, TestimonyForm


def home_view(request):
    info = PersonalInformation.objects.first()
    projects = Project.objects.all()

    context = {
        'info': info,
        'projects': projects
    }s
    return render(request, 'index.html', context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})


def contact_view(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_message = request.POST.get('message')
    
        ContactMessage.objects.create(email=user_email, message=user_message)
        messages.success(request, "Mission log launched successfully!")
        return redirect('home')
        
    return render(request, 'index.html')


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()
        
    return render(request, 'create_project.html', {'form': form})
        

def contact_inquiry(request):
    if request.method == 'POST':
        Inquiry.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            contact_number=request.POST.get('contact_number'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            message=request.POST.get('message')
        )
        return redirect('contact_success')
        
    return render(request, 'contact.html')

    
def create_testimony(request):
    if request.method == 'POST':
        form = TestimonyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimony_list')
    else:
        form = TestimonyForm()

    return render(request, 'create_testimony.html', {'form': form})


class TestimonyListView(ListView):
    model = Testimony
    template_name = 'testimony_list.html'
    context_object_name = 'testimonies'

def testimony_detail(request,pk):
    testimony = get_object_or_404(Testimony, pk=pk)
    return render(request, 'testimony_detail.html', {'testimony':testimony})

def contact_success(request):
    return render(request, 'contact_success.html')