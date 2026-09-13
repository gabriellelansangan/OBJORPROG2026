from django import forms
from .models import Project, Testimony

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['full_name', 'content']