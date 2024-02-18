from django.shortcuts import render

# Vistas 
def rooms(request):
    return render(request, 'rooms.html')