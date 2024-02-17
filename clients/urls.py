from rest_framework import routers
from django.urls import include 
from django.urls import path
from clients import views

router = routers.DefaultRouter()

# Rutas
router.register(r'list', views.ClientsView, 'clients_list')

urlpatterns = [
    path('', include(router.urls))
]