import os
import sys
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('contact/', views.contact_inquiry, name='contact'),
    path('contact/submit/', views.contact_view, name='contact_submit'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('testimonies/', views.TestimonyListView.as_view(), name='testimony_list'),
    path('testimonies/add/', views.create_testimony, name='create_testimony'),
    path('testimonies/<int:pk>/', views.testimony_detail, name='testimony_detail'),
    path('login/', views.AdminLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', views.ProjectListView.as_view(), name='project_list'),
    path('dashboard/project/new/', views.ProjectCreateView.as_view(), name='project_create'),
    path('dashboard/tech-stacks/', views.TechStackListView.as_view(), name='techstack_list'),
    path('dashboard/tech-stacks/new/', views.TechStackCreateView.as_view(), name='techstack_create'),
]
