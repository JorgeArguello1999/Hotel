from django.db import models

# Modelos externos
from reservations.models import ReservationsModel

# Precios
class PricingModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self) -> str:
        return f'{self.name} -> {self.price}'

# IVA
class IVAModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self) -> str:
        return f'{self.name} -> {self.price}'

# Factura
class BillingModel(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(ReservationsModel, on_delete=models.CASCADE)
    date = models.DateField()
    iva = models.ForeignKey(IVAModel, on_delete=models.CASCADE)
    value = models.FloatField()

    def __str__(self) -> str:
        return f'{self.client} -> {self.value}'