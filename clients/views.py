from django.shortcuts import render

# Vistas para el manejo de los clientes
def clients(request):
    return render(request, 'clients.html')