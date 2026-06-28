from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology_used = models.CharField(max_length=100)
    live_link = models.URLField(blank=True)

    def __str__(self):
        return self.title