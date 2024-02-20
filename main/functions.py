# Modelos 
from reservations.models import ReservationsModel
from rooms.models import StatusModel

# Actualizar el estado de una habitación
def update_room_status(room_to_change, status):
    room = room_to_change.room
    occupied_status = StatusModel.objects.get(name=status)
    room.status = occupied_status
    room.save()