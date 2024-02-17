from rest_framework import routers
from django.urls import include 
from django.urls import path

from reservations import views

router = routers.DefaultRouter()

# Rutas
router.register(r'list', views.ReservationsView, 'reservations_list')
router.register(r'states', views.StatesViews, 'reservations_states')


urlpatterns = [
    path('', include(router.urls))
]