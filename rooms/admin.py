from django.contrib import admin

from .models import tipo
from .models import estado
from .models import habitaciones

# Register your models here.
admin.site.register(tipo)
admin.site.register(estado)
admin.site.register(habitaciones)