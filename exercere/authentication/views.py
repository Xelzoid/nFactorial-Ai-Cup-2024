from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("h")

def register(request):
    return HttpResponse("r")

def login(request):
    return HttpResponse("l")

def dashboard(request):
    return HttpResponse("d")
