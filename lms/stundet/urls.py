from django.urls import path
from . import views
urlpatterns = [
    path("" , views.home , name = "home"),
    path("about/" , views.about , name = "about"),
    path("contact/" , views.contact , name = "contact"),
    path("register/" , views.register , name = "register"),
    path("login/" , views.Login , name = "login"),
    path("Student_home/" , views.Student_home , name = "Student_home"),
    path("assisment/" , views.assisment , name = "assisment"),
    path("notes/" , views.notes , name = "notes"),
]
