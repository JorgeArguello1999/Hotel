from django import forms

# Modelos
from billing.models import BillingModel

# Formulario
class BillingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configura el widget del campo 'date' para que sea un campo de fecha
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
       
    class Meta:
        model = BillingModel
        fields = ['client', 'date', 'iva', 'discounts', 'value']