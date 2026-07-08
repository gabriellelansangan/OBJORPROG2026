from django.contrib import admin
from .models import Project, ContactMessage, PersonalInformation

admin.site.register(Project)
admin.site.register(ContactMessage)
admin.site.register(PersonalInformation)
