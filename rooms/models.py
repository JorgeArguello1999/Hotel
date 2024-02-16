from django.db import models

# Estado de las habitaciones
class estado(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.estado}'

# Tipo de habitaciones
class tipo(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20)
    cama = models.IntegerField()
    persona = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.tipo} Camas: {self.cama} Personas: {self.persona}'

"""
Esta tabla es la principal
"""

# Modelos para las habitaciones
class habitaciones(models.Model):
    id = models.AutoField(primary_key=True)
    cuarto = models.IntegerField(default=100)
    estado = models.ForeignKey(estado, on_delete=models.CASCADE)
    tipo = models.ForeignKey(tipo, on_delete=models.CASCADE)
    observaciones = models.TextField(default='...')