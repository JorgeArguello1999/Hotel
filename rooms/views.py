from django.shortcuts import render

# Vistas para Habitaciones
def rooms(request):
    return render(request, 'rooms.html')