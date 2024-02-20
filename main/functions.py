# Excepciones
from django.core.exceptions import ObjectDoesNotExist

# Modelos 
from reservations.models import ReservationsModel
from rooms.models import StatusModel
from billing.models import PricingModel

# Actualizar el estado de una habitación
def update_room_status(room_to_change, status):
    room = room_to_change.room
    occupied_status = StatusModel.objects.get(name=status)
    room.status = occupied_status
    room.save()

# Calculamos el precio de la habitación
def calculate_price_of_room(data: list, iva=0, discount=0) -> float:
    try: adults = PricingModel.objects.get(name='Adults').price
    except: adults = 0

    try: childrens = PricingModel.objects.get(name='Childrens').price
    except: childrens = 0

    try: third_age = PricingModel.objects.get(name='Third age').price
    except: third_age = 0

    adults = adults * data[0]
    childrens = childrens * data[1]
    third_age = third_age * data[2]

    # Descuento
    value = adults + childrens + third_age
    discount = (value * discount) / 100
    value = value - discount

    # IVA
    iva_count = (value * iva) / 100
    return value + iva_count

# Actualizamos el estado de la reserva
def update_reservation_status(id_reservation, value:bool):
    reservation = ReservationsModel.objects.get(pk=id_reservation)
    reservation.reservation_status = value
    reservation.save()

if __name__ == '__main__':
    calculate_price_of_room()