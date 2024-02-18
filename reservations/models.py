from django.db import models

# Modelos Externos
from clients.models import ClientsModel
from rooms.models import RoomsModel

# Modelo de Reservations
class ReservationsModel(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(ClientsModel, on_delete=models.CASCADE)
    room = models.ForeignKey(RoomsModel, on_delete=models.CASCADE)
    reservation_status = models.BooleanField(default=True)

    # Fecha de entrada y salida
    entry_date = models.DateField()
    out_date = models.DateField()

    # Personas
    adults = models.IntegerField()
    childrens = models.IntegerField(blank=True, null=True)
    third_age = models.IntegerField(blank=True, null=True)

    # Notas
    notes = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f'Cliente:{self.client} -> Cuarto:{self.room.number} -> Estado:{self.reservation_status}'