from rest_framework import viewsets

# Serialización JSON
from reservations.serializer import Reservaciones_Serializer
from reservations.serializer import Estados_Serializer

# Modelos 
from reservations.models import reservacion
from reservations.models import estado

# Modelos Externos
from rooms.models import habitaciones

class ReservationsView(viewsets.ModelViewSet):
    serializer_class = Reservaciones_Serializer
    queryset = reservacion.objects.select_related('habitacion', 'estado_reserva').all()
    
class StatesViews(viewsets.ModelViewSet):
    serializer_class = Estados_Serializer
    queryset = estado.objects.all()