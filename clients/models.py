from django.db import models

# Modelo Cliente
class ClientsModel(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True)
    names = models.CharField(max_length=255)
    last_names = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=255, blank=True, null=True)
    direction = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f'{self.cedula} -> {self.names} {self.last_names} -> {self.phone}' 