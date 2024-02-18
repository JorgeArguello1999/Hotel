from django.shortcuts import redirect
from django.shortcuts import render

# Modelos
from reservations.models import ReservationsModel

# Formularios
from reservations.forms import ReservationsForms

# Vistas 
def reservations(request):
    # GET
    if request.method == 'GET':
        form = ReservationsForms()
        items = ReservationsModel.objects.all().order_by('room')

        return render(request, 'reservations.html', {
            'form': form,
            'items': items
        })

def reservations_update(request, id_reservation):
    return redirect('reservations')

def reservations_delete(request, id_reservation):
    return redirect('reservations')