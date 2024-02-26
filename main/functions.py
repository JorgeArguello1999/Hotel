# Excepciones
from django.core.exceptions import ObjectDoesNotExist

# Modulos 
from datetime import datetime

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
def calculate_price_of_room(data: list, date_in: datetime, date_out: datetime, iva=0, discount=0) -> float:
    try:
        adults_price = PricingModel.objects.get(name='Adults').price
    except PricingModel.DoesNotExist:
        adults_price = 0

    try:
        childrens_price = PricingModel.objects.get(name='Childrens').price
    except PricingModel.DoesNotExist:
        childrens_price = 0

    try:
        third_age_price = PricingModel.objects.get(name='Third age').price
    except PricingModel.DoesNotExist:
        third_age_price = 0

    # Calcular el número de noches de estancia
    num_nights = (date_out - date_in).days

    # Calcular el precio por tipo de cliente
    adults_total_price = adults_price * data[0] * num_nights
    childrens_total_price = childrens_price * data[1] * num_nights
    third_age_total_price = third_age_price * data[2] * num_nights

    # Calcular el subtotal antes de aplicar descuento
    subtotal = adults_total_price + childrens_total_price + third_age_total_price

    # Aplicar descuento si es aplicable
    subtotal -= (subtotal * discount / 100)

    # Calcular el monto de IVA
    iva_amount = subtotal * iva / 100

    # Calcular el precio total incluyendo IVA
    total_price = subtotal + iva_amount

    return total_price

# Actualizamos el estado de la reserva
def update_reservation_status(id_reservation, value:bool):
    reservation = ReservationsModel.objects.get(pk=id_reservation)
    reservation.reservation_status = value
    reservation.save()

if __name__ == '__main__':
    calculate_price_of_room()