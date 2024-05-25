from rest_framework import serializers
from .models import UserData

class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['preferences', 'fitness_goals', 'meal_plan']
