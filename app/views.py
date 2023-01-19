from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('hello all')

def home(request):

    return HttpResponse("home")

def register(request):
    print("register")
    return HttpResponse("Register")

def login(request):
    print("login")
    return HttpResponse("login")