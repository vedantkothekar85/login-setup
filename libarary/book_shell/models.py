from django.db import models
import datetime

# user : admin
# pass : 123

# Create your models here.

class New_signup(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    dob = models.DateField()
    password = models.CharField(max_length=50)
    conf_pass = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username
    
    