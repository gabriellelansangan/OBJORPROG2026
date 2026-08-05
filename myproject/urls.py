from django.contrib import admin
from django.urls import path
from core.views import home_view
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('contact', views.contact_view, name='contact_submit'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/add/', views.create_project, name='create_project'),
    path('contact/', views.contact_inquiry, name='contact'),
    path('testimonies/', views.TestimonyListView.as_view(), name='testimony_list'),
    path('testimonies/add/', views.create_testimony, name='create_testimony'),
    path('testimonies/<int:pk>/', views.testimony_detail, name='testimony_detail'),
]
