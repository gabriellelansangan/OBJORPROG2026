from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    technology_used = models.CharField(max_length=200)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.project_name
    
class PersonalInformation(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    summary = models.TextField()
    contact_number = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class ContactMessage(models.Model):
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.email} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"