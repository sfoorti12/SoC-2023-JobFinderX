from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fname = models.CharField(max_length=120, null=True, blank=True)
    lname = models.CharField(max_length=120, null=True, blank=True)
    contact = models.CharField(max_length=120, null=True, blank=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    is_employed = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
    
class PostJobModel(models.Model):
    company = models.CharField(max_length=120, null=True, blank=True)
    position = models.CharField(max_length=120, null=True, blank=True)
    job_type = models.CharField(max_length=120, null=True, blank=True)
    education = models.CharField(max_length=120, null=True, blank=True)
    experience = models.CharField(max_length=120, null=True, blank=True)
    salary = models.CharField(max_length=120, null=True, blank=True)
    location = models.CharField(max_length=120, null=True, blank=True)
    
    def __str__(self):
        return self.company