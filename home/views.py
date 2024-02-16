from django.shortcuts import render

# Vistas para la página de Inicio
def home(request):
    return render(request, 'home.html')