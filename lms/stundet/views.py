from django.http import HttpResponse
from django.shortcuts import render
from . models import *
# Create your views here.
def home(request):
    return render(request , "navBar.html")

def about(request):
    about = about_info.objects.all()
    return render(request , "about.html" , {"about": about})

def contact(request):
    return render(request , "contact.html")

def register(request):
    return render(request , "register.html")

def Login(request):
    return render(request , "login.html")

