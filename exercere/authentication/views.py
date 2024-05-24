from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import CreateUserForm, LoginForm, MealPreferences
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
def homepage(request):
    return HttpResponse("h")

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginfunc")
    context = {'registerform':form}
    return HttpResponse("r")

def loginfunc(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)

            if user is not None:
                auth.login(request,user)
                return redirect("dashboard")

    context = {'loginform':form}
    return HttpResponse("l")
def logout(request):
    auth.logout(request)
    return redirect("")
@login_required(login_url="loginfunc")
def dashboard(request):
    return HttpResponse("d")

@login_required(login_url="loginfunc")
def mealplan(request):
    pass