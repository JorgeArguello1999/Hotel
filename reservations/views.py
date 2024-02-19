from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Security
from django.contrib.auth.decorators import login_required

# Modelos
from reservations.models import ReservationsModel

# Modelos externos
from rooms.models import RoomsModel
from rooms.models import StatusModel

# Formularios
from reservations.forms import ReservationsForms

# Vistas 
@login_required
def reservations(request):
    # GET
    if request.method == 'GET':
        form = ReservationsForms()
        items = ReservationsModel.objects.all().order_by('room')

        return render(request, 'reservations.html', {
            'form': form,
            'items': items
        })

    # POST
    if request.method == 'POST':
        form = ReservationsForms(request.POST)
        if form.is_valid():
            # Guardar la reserva
            reservation = form.save(commit=False)  
            reservation.save()  

            # Cambiar habitación a Ocupado
            update_room_status(reservation, 'Ocupado')

            return redirect('reservations')

@login_required
def reservations_update(request, id_reservation):
    reservation = get_object_or_404(ReservationsModel, pk=id_reservation)
    
    # POST
    if request.method == 'POST':
        # Llenar con la información del cliente
        form = ReservationsForms(request.POST, instance=reservation)
        # Cambiamos el status de la habitación
        update_room_status(reservation, 'Vacio')

        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            update_room_status(form, 'Ocupado')

            return redirect('reservations')

        else:
            update_room_status(form, 'Ocupado')
            return redirect('reservations_update')
        
    # GET
    if request.method == 'GET':
        form = ReservationsForms(instance=reservation)

    return render(request, 'reservation_update.html', {
        'form': form, 
        'reservation': reservation
    })

@login_required
def reservations_delete(request, id_reservation):
    reservation = get_object_or_404(ReservationsModel, pk=id_reservation)
    reservation.delete()
    # Pasar a Vacio el estado de la habitación
    update_room_status(reservation, 'Vacio')
    return redirect('reservations')

# Actualizar el estado de una habitación
def update_room_status(room_to_change, status):
    room = room_to_change.room
    occupied_status = StatusModel.objects.get(name=status)
    room.status = occupied_status
    room.save()