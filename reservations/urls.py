from django.urls import path
from reservations import views

urlpatterns = [
    path('', views.reservations, name='reservations'),
    path('update/<str:id_reservation>', views.reservations_update, name='reservations_update'),
    path('delete/<str:id_reservation>', views.reservations_delete, name='reservations_delete'),
]