from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField

class UserData(models.Model):
    preferences = models.TextField()
    fitnessgoal = models.TextField()
    meal_plan = JSONField()

        