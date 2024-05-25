from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm, MealPreferences
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .ai import GenerateMealPlan
from .models import UserData
from .serializers import MealPlanSerializer 
def homepage(request):
    return render(request, 'authentication/html/homepage.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {'registerform':form}
    return render(request, 'authentication/html/register.html', context=context)
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")


    context = {'loginform':form}

    return render(request, 'authentication/html/my-login.html', context=context)


def logout(request):
    auth.logout(request)
    return redirect("")
@login_required(login_url="login")
def dashboard(request):
    return render(request, 'authentication/html/dashboard.html')

@login_required(login_url="login")
def mealplan(request):
    preferences = request.data.get('preferences')
    fitness_goals = request.data.get('fitness_goals')
    if not preferences or not fitness_goals:
        return HttpResponse("<h1>Error: Preferences and fitness goals are required.</h1>", status=400)

    meal_plan_json = GenerateMealPlan(preferences, fitness_goals)

    # Save the meal plan to the database
    meal_plan = UserData.objects.create(
        preferences=preferences,
        fitnessgoal=fitness_goals,
        meal_plan=meal_plan_json
    )

    serializer = MealPlanSerializer(meal_plan)
    return render(request, 'meal_plan.html', {'meal_plan': serializer.data})