from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , "navBar.html")

def about(request):
    return render(request , "about.html")

def contact(request):
    return render(request , "contact.html")

def register(request):
    return render(request , "register.html")

