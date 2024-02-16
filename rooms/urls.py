from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('update/<int:id_habitacion>', views.rooms_update, name='rooms_update'),
    path('delete/<int:id_habitacion>', views.rooms_delete, name='rooms_delete')
]