from rest_framework import serializers
from rooms.models import habitaciones

class Habitaciones_Serializer(serializers.ModelSerializer):
    class Meta:
        model = habitaciones
        fields = '__all__'