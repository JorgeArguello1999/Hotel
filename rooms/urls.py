from django.urls import path

# Vistas
from rooms import views

# Rutas
urlpatterns = [
    path('', views.rooms, name='rooms_list')
]