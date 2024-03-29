from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.db import IntegrityError

# Vista del Home
@login_required
def home(request):
    return render(request, 'index.html')

# Usuarios
def signin(request):
    if request.method == "GET":
        return render(request, 'signin.html', {
            "form": AuthenticationForm
        })
    
    user = authenticate(
        request, username=request.POST['username'], password=request.POST['password']
    )

    if user is None:
        return render(request, "signin.html", {
            "error": "Usuario o contraseña incorrectos"
        })
    
    login(request, user)
    return redirect("home")

def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {
            "form": UserCreationForm
        })
    
    if request.POST["password1"] == request.POST["password2"]:
        try:
            user = User.objects.create_user(
                request.POST["username"], password=request.POST["password2"]
            )
            user.save()
            login(request, user)
            return redirect("home")
        
        except IntegrityError:
            return render(request, "signup.html", {
                "form": UserCreationForm,
                "error": "Usuario ya existe"
            })

@login_required
def signout(request):
    logout(request)
    return redirect("signin")