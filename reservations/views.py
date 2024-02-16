from django.shortcuts import render

# Vista de reservaciones
def reservations(request):
    return render(request, 'reservations.html')