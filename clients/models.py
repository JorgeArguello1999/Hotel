from django.db import models

# Clientes
class clients(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10)
    nombres = models.CharField(max_length=255, default='Cliente')
    nacimiento = models.DateField(default=None)
    alergias = models.TextField(default='...')
    notas = models.TextField(default='...')

    def __str__(self) -> str:
        return f'{self.cedula} -> {self.nombres}'