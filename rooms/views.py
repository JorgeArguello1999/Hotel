from rest_framework import viewsets

from rooms.serializer import Habitaciones_Serializer

from rooms.models import habitaciones

class RoomsView(viewsets.ModelViewSet):
    serializer_class = Habitaciones_Serializer
    queryset = habitaciones.objects.all()