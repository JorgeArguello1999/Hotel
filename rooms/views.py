from django.shortcuts import render
from django.shortcuts import HttpResponse

# Vistas para Habitaciones
def rooms(request):
    return HttpResponse(request, 'hola')