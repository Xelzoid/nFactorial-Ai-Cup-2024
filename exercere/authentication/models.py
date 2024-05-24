from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    mealpref = models.CharField(max_length=520)
    fitnessgoal = models.CharField(max_length=100)
        