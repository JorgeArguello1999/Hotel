from django import forms
from rooms.models import RoomsModel
from reservations.models import ReservationsModel

class ReservationsForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar las habitaciones con estado "Vacio"
        empty_rooms = RoomsModel.objects.filter(status__name='Vacio')
        # Asignar las habitaciones filtradas al campo 'room' del formulario
        self.fields['room'].queryset = empty_rooms
        # Configurar el campo de cliente para mostrar una etiqueta vacía
        self.fields['client'].empty_label = "Seleccionar cliente"

    class Meta:
        model = ReservationsModel
        fields = '__all__'
