from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username = forms.CharField(label="Nom d'utilisateur", Widget = forms.TextInput(
        attrs={
            "class": "form-control"
        }
    ))
    email = forms.EmailField(label="Email", Widget = forms.EmailInput(
        attrs={
            "class": "form-control"
        }
    ))
    password1 = forms.CharField(label="Mot de passe", Widget = forms.PasswordInput(
        attrs={
            "class": "form-control"
        }
    ))
    
    password2 = forms.CharField(label="Confirmer Mot de passe", Widget = forms.PasswordInput(
        attrs={
            "class": "form-control"
        }
    ))
    
    class Meta:
        model= User
        fields = ('username', 'email', 'passeword1', 'password2')
    
    
    