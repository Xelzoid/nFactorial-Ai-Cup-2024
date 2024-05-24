from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import CreateUserForm
def homepage(request):
    return HttpResponse("h")

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {'registerform':form}
    return HttpResponse("r", context=context)

def login(request):
    return HttpResponse("l")

def dashboard(request):
    return HttpResponse("d")
