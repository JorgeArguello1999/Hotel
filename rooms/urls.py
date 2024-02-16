from rest_framework import routers
from django.urls import path
from django.urls import include 

from rooms import views

router = routers.DefaultRouter()
router.register(r'', views.RoomsView, 'rooms')

urlpatterns = [
    path('', include(router.urls))
]