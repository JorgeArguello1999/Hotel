from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

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
    reservation = get_object_or_404(ReservationsModel, pk=id_reservation)
    
    # POST
    if request.method == 'POST':
        # Llenar con la información del cliente
        form = ReservationsForms(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservations')
        
    # GET
    if request.method == 'GET':
        form = ReservationsForms(instance=reservation)

    return render(request, 'reservation_update.html', {
        'form': form, 
        'reservation': reservation
    })

def reservations_delete(request, id_reservation):
    reservation = get_object_or_404(ReservationsModel, pk=id_reservation)
    reservation.delete()
    return redirect('reservations')