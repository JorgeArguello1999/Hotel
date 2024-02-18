from django.urls import path

# Vistas
from rooms import views

# Rutas
urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('delete/<int:id_room>', views.rooms_delete, name='rooms_delete')
]