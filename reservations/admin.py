from django.contrib import admin

from .models import estado
from .models import reservacion

# Register your models here.
admin.site.register(estado)
admin.site.register(reservacion)