from rest_framework import viewsets

# Serialización JSON
from clients.serializer import Clientes_Serializers

# Modelos
from clients.models import clients

# JWT 
from rest_framework.permissions import IsAuthenticated

# Vistas para el manejo de los clientes
class ClientsView(viewsets.ModelViewSet):
    serializer_class = Clientes_Serializers 
    queryset = clients.objects.all()
    permission_classes = [IsAuthenticated]