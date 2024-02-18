from django.urls import path

# Vistas
from clients import views 

# Rutas
urlpatterns = [
    path('', views.clients, name='clients'),
    path('update/<str:id_client>', views.clients_update, name='clients_update'),
    path('delete/<str:id_client>', views.clients_delete, name='clients_delete')
]