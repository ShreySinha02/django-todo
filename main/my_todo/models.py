from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    note=models.TextField(null=False)
    
    
    def __str__(self):
        return str(self.user)
    
    
    