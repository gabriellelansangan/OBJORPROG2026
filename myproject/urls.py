from django.contrib import admin
from django.urls import path
from core.views import home_view
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('contact', views.contact_view, name='contact_submit'),
    path('project/<int:pk>/', views.project_detail, name='project_detail')
]
