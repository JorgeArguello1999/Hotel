from django import forms
from .models import habitaciones

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = habitaciones
        fields = ['cuarto', 'estado', 'tipo', 'observaciones']