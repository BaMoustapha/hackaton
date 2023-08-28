from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import SignupForm



# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/services/templates/home.html')  # Rediriger vers la page d'accueil après la connexion réussie
        else:
            # Gérer le cas d'authentification invalide ici
            pass

    return render(request, '/services/templates/user.html')

def register_user(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=raw_password)
        return redirect("/services/templates/user.html")
    else:
        form = SignupForm()
        
        
    return render(request, "/services/templates/register.html", {"form": form})