from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm, PlanForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .ai import GenerateMealPlan, GenerateFitnessPlan
from .models import UserData
from .serializers import MealPlanSerializer, FitnessPlanSerializer
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
    meal_plan = None
    fitness_plan = None

    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            preferences = form.cleaned_data['preferences']
            fitness_goals = form.cleaned_data['fitness_goals']
            
            if 'create_meal_plan' in request.POST:
                meal_plan_json = GenerateMealPlan(preferences, fitness_goals)
                meal_plan = UserData.objects.create(
                    preferences=preferences,
                    fitness_goals=fitness_goals,
                    meal_plan=meal_plan_json
                )
                request.session['meal_plan'] = meal_plan_json
            
            if 'create_fitness_plan' in request.POST:
                fitness_plan_json = GenerateFitnessPlan(fitness_goals)
                fitness_plan = UserData.objects.create(
                    preferences=preferences,
                    fitness_goals=fitness_goals,
                    fitness_plan=fitness_plan_json
                )
                request.session['fitness_plan'] = fitness_plan_json
            
            return redirect('dashboard')

    else:
        form = PlanForm()
    
    # Retrieve plans from session
    if 'meal_plan' in request.session:
        meal_plan = request.session['meal_plan']
    if 'fitness_plan' in request.session:
        fitness_plan = request.session['fitness_plan']

    return render(request, 'authentication/html/dashboard.html', {'form': form, 'meal_plan': meal_plan, 'fitness_plan': fitness_plan})