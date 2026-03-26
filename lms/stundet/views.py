from django.http import HttpResponse
from django.shortcuts import render , redirect
from . models import *
# Create your views here.
def home(request):
    return render(request , "navBar.html")

def about(request):
    about = about_info.objects.all()
    return render(request , "about.html" , {"about": about})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        data = contact_info(name = name , email = email , message = message , subject = subject)
        data.save()
    return render(request , "contact.html")

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        course = request.POST.get("course")
        city = request.POST.get("city")
        zip_code = request.POST.get("zip")
        country = request.POST.get("country")
        userdata = RegisteredUser(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            phone=phone,
            course=course,
            city=city,
            zip_code=zip_code,
            country=country
        )
        userdata.save()
        return redirect("login")
    return render(request, "register.html")

def Login(request):
     if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = RegisteredUser.objects.get(email=email, password=password)
            request.session['user'] = user.first_name
            return redirect("Student_home")

        except RegisteredUser.DoesNotExist:
                return render(request, "login.html", {"error":"Invalid Email or Password"})
     return render(request , "login.html")

# for student page

def Student_home(request):
    if 'user' in request.session:
        user_name = request.session['user']
        return render(request , "student/Student_home.html" , {"user_name": user_name})
    else:
        return redirect("login")

def assisment(request):
    if 'user' in request.session:
        user_name = request.session['user']
        return render(request , "student/Assisment.html" , {"user_name": user_name})
    else:
        return redirect("login")
    
def notes(request):
    if 'user' in request.session:
        user_name = request.session['user']
        return render(request , "student/Notes.html" , {"user_name": user_name})
    else:
        return redirect("login")
    
def courses(request):
    if 'user' in request.session:
        user_name = request.session['user']
        return render(request , "student/courses.html" , {"user_name": user_name})
    else:
        return redirect("login")
