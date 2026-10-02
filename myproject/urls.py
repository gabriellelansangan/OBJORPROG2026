import os
import sys
from django.contrib import admin
from django.urls import path
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
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/project/create/', views.create_project, name='create_project'),
    path('dashboard/tech-stack/create/', views.create_tech_stack, name='create_tech_stack'),
]
