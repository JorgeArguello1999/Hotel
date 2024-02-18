from rest_framework import serializers

# Modelos
from reservations.models import estado
from reservations.models import reservacion

# Serializadores Externos
from rooms.serializer import Habitaciones_Serializer

class Estados_Serializer(serializers.ModelSerializer):
    class Meta:
        model = estado
        fields = '__all__'

class Reservaciones_Serializer(serializers.ModelSerializer):
    estado_reserva = Estados_Serializer()
    habitacion = Habitaciones_Serializer()  # Anidando información de la habitación

    class Meta:
        model = reservacion
        fields = '__all__'