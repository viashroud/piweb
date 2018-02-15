from django.db import models
from django.utils import timezone
import getpass

class Interface(models.Model):
    name = models.CharField(max_length=50)
    interface_type = models.CharField(max_length=50)
    pin = models.IntegerField()
        
    def create_interface(self):
        self.save()
    
    def __str__(self):
        return self.name
    
