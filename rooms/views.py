from rest_framework import viewsets

# Serialización JSON
from rooms.serializer import Habitaciones_Serializer
from rooms.serializer import Estados_Serializer
from rooms.serializer import Tipos_Serializer

# Modelos
from rooms.models import habitaciones
from rooms.models import estado
from rooms.models import tipo

class RoomsView(viewsets.ModelViewSet):
    serializer_class = Habitaciones_Serializer
    queryset = habitaciones.objects.all()

class StateView(viewsets.ModelViewSet):
    serializer_class = Estados_Serializer
    queryset = estado.objects.all()

class TypeView(viewsets.ModelViewSet):
    serializer_class = Tipos_Serializer
    queryset = tipo.objects.all()