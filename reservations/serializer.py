from rest_framework import serializers

# Modelos
from reservations.models import estado
from reservations.models import reservacion

class Estados_Serializer(serializers.ModelSerializer):
    class Meta:
        model = estado
        fields = '__all__'

class Reservaciones_Serializer(serializers.ModelSerializer):
    class Meta:
        model = reservacion
        fields = '__all__'