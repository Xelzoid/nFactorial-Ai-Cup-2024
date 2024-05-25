from rest_framework import serializers
from .models import MealPlan

class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlan
        fields = ['preferences', 'fitness_goals', 'meal_plan']
