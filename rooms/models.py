from django.db import models

# Tipos de Habitaciones
class TypesModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    bed = models.IntegerField(default=0)
    person = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.name} -> Camas:{self.bed} -> Personas:{self.person}'

# Estado de las Habitaciones
class StatusModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.name}'

# Modelo de Habitaciones 
class RoomsModel(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField(unique=True)
    status = models.ForeignKey(StatusModel, on_delete=models.CASCADE)
    types = models.ForeignKey(TypesModel, on_delete=models.CASCADE)
    notes = models.TextField(default='', blank=True, null=True)

    def __str__(self) -> str:
        return f'#{self.number} -> {self.types.name} -> Camas y Personas:{self.types.bed}x{self.types.person} ->  {self.status.name}'