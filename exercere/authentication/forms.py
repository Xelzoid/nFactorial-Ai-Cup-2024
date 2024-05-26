from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class PlanForm(forms.Form):
    preferences = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Meal Preferences (Allergies, dislikes, etc.)'})
    )
    fitness_goals = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Fitness Goals (Weight loss, bulking, etc.)'})
    )