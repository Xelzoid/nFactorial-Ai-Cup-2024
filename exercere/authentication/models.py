from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField

class UserData(models.Model):
    preferences = models.TextField()
    fitness_goals = models.TextField()
    meal_plan = models.JSONField(null=True, blank=True)
    fitness_plan = models.JSONField(null=True, blank=True)