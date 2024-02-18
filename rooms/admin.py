from django.contrib import admin

# Modelos
from rooms.models import TypesModel
from rooms.models import StatusModel
from rooms.models import RoomsModel

# Tipos de Habitación
admin.site.register(TypesModel)
admin.site.register(StatusModel)
admin.site.register(RoomsModel)