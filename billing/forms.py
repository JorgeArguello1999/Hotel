from django import forms

# Modelos
from reservations.models import ReservationsModel
from billing.models import BillingModel

# Formulario
class BillingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configura el widget del campo 'date' para que sea un campo de fecha
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})

        # Solo Mostramos las reservaciones que estan activas
        active_reservations = ReservationsModel.objects.filter(reservation_status=True)
        self.fields['client'].queryset = active_reservations

       
    class Meta:
        model = BillingModel
        fields = ['client', 'date', 'iva', 'discounts', ]