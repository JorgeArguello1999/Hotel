from django.core.exceptions import ValidationError
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
    tiempo_salida = models.DateField()
    # Campo generado automaticamente
    fecha_agendamiento = models.DateField(auto_now=True)
    estado_reserva = models.ForeignKey(estado, on_delete=models.CASCADE)

    def clean(self):
        # Verificar que el tiempo de salida no sea menor al tiempo de ingreso
        if self.tiempo_salida < self.tiempo_ingreso:
            raise ValidationError("El tiempo de salida no puede ser menor al tiempo de ingreso.")

        # Verificar si la habitación está ocupada para evitar agendar
        if self.habitacion.estado.estado == 'Ocupada':
            raise ValidationError("La habitación está ocupada y no se puede agendar.")

    def save(self, *args, **kwargs):
        # Verificar si la habitación está vacía para permitir agendar
        if self.habitacion.estado.estado != 'Ocupado':
            super().save(*args, **kwargs)
        else:
            raise ValidationError("La habitación no está vacía y no se puede agendar.")

    def __str__(self) -> str:
        return f'{self.cedula} -> {self.habitacion} -> {self.habitacion.estado.estado} -> {self.estado_reserva}' 