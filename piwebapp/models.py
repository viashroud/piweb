from django.db import models
from django.utils import timezone
import getpass

class Device(models.Model):
    name = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    hostname = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    
    def create_device(self):
        self.save()
    
    def __str__(self):
        return self.name
    
