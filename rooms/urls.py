from rest_framework import routers
from django.urls import path
from django.urls import include 

from rooms import views

router = routers.DefaultRouter()

# Rutas
router.register(r'list', views.RoomsView, 'rooms')
router.register(r'states', views.StateView, 'states')
router.register(r'types', views.TypeView, 'types')

urlpatterns = [
    path('', include(router.urls))
]