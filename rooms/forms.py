from django import forms

# Modelos
from rooms.models import TypesModel 
from rooms.models import StatusModel
from rooms.models import RoomsModel

class RoomForm(forms.ModelForm):
    class Meta:
        model = RoomsModel
        fields = ['number', 'status', 'types', 'notes']

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = "Seleccionar estado"
        self.fields['types'].empty_label = "Seleccionar tipo de habitación"
