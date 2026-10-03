from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Project, Testimony, TechStack

class AdminAuthenticationForm(AuthenticationForm):
    """Only superusers may authenticate, even if other accounts exist."""

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_superuser:
            raise forms.ValidationError(
                "This page is for administrators only.",
                code='not_admin',
            )

class ProjectForm(forms.ModelForm):
    tech_stacks = forms.ModelChoiceField(
        queryset = TechStack.objects.all(),
        widget = forms.RadioSelect,
        empty_label=None,
        label = 'Tech Stack',
    )
    class Meta:
        model = Project
        fields = ['project_name', 'description', 'link']
        labels = {'project_name': 'Project Name', 'description': 'Project Description'}
        widgets = {'description': forms.Textarea(attrs={'rows':5})}

    def save(self, commit=True):
        project = super().save(commit=commit)
        if commit:
            project.tech_stacks.set([self.cleaned_data['tech_stack']])
        return project 

class TechStackForm(forms.ModelForm):
    class Meta:
        model = TechStack
        fields = ['name']
        labels = {'name': 'Tech Stack Name'}
        
class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['full_name', 'content']