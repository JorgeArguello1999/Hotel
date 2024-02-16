from rest_framework import routers
from django.urls import path
from django.urls import include 

from rooms import views

router = routers.DefaultRouter()

# Rutas
router.register(r'list', views.RoomsView, 'rooms_list')
router.register(r'states', views.StatesView, 'rooms_states')
router.register(r'types', views.TypesView, 'rooms_types')

urlpatterns = [
    path('', include(router.urls))
]