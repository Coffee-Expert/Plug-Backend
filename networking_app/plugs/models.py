 
# Create your models here.
from django.db import models

class PlugRequest(models.Model):
    magic_line = models.TextField()  
    target_name = models.CharField(max_length=100)   
    status = models.CharField(max_length=20, default='pending')   
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Request to {self.target_name}: {self.magic_line[:30]}"

class Message(models.Model):
    plug_request = models.ForeignKey(PlugRequest, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Message: {self.content[:30]}"
