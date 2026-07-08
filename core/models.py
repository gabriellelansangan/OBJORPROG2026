from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology_used = models.CharField(max_length=100)
    live_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.email} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"