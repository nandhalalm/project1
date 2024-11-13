from django.db import models
from django.contrib.auth.models import AbstractUser



class  CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    image = models.FileField( blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    
    