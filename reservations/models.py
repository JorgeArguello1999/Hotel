from django.db import models

# Importamos las habitaciones
from rooms.models import habitaciones

# Estado de la reservacion 
class estado(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.estado}'

# Reservación 
class reservacion(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10)
    habitacion = models.ForeignKey(habitaciones, on_delete=models.CASCADE)
    notas = models.TextField(default='...')
    tiempo_ingreso = models.DateField()
    timepo_salida = models.DateField()
    # Campo generado automaticamente
    fecha_agendamiento = models.DateField(auto_now=True)
    estado_reserva = models.ForeignKey(estado, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.cedula} -> {self.habitacion} -> {self.estado_reserva}' 