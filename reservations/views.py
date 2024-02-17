from rest_framework import viewsets

# Serialización JSON
from reservations.serializer import Reservaciones_Serializer
from reservations.serializer import Estados_Serializer

# Modelos 
from reservations.models import reservacion
from reservations.models import estado

# JWT
from rest_framework.permissions import IsAuthenticated

class ReservationsView(viewsets.ModelViewSet):
    serializer_class = Reservaciones_Serializer
    queryset = reservacion.objects.select_related('estado_reserva').all()
    permission_classes = [IsAuthenticated]
    
class StatesViews(viewsets.ModelViewSet):
    serializer_class = Estados_Serializer
    queryset = estado.objects.all()
    permission_classes = [IsAuthenticated]