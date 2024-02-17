from rest_framework import serializers

# Modelos
from clients.models import clients

class Clientes_Serializers(serializers.ModelSerializer):
    class Meta:
        model = clients
        fields = '__all__'