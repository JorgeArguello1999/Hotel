from rest_framework import serializers

# Modelos
from rooms.models import habitaciones
from rooms.models import estado
from rooms.models import tipo

class Habitaciones_Serializer(serializers.ModelSerializer):
    class Meta:
        model = habitaciones
        fields = '__all__'

class Estados_Serializer(serializers.ModelSerializer):
    class Meta:
        model = estado
        fields = '__all__'

class Tipos_Serializer(serializers.ModelSerializer):
    class Meta:
        model = tipo
        fields = '__all__'