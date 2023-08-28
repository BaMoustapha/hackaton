from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "/services/templates/index.html")

def home(request):
    return render(request, "/services/templates/home.html")

def contact(request):
    return render(request, "/services/templates/contact.html")

def register(request):
    return render(request, "/services/templates/register.html")

def user(request):
    return render(request, "/services/templates/user.html")