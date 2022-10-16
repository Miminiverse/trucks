from email.policy import default
from django.db import models

# Create your models here.

class Video(models.Model):
    caption = models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%y")
    
    def __str__(self):
        return f"{self.caption}"
    
    
class Task(models.Model):
    title=models.CharField(max_length=200)
    completed = models.BooleanField(default=True, blank=True, null=True)
    
    def __str__(self):
        return self.title
