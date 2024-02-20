from django import forms

# Modelos
from billing.models import BillingModel

# Formulario
class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingModel
        fields = ['client', 'date', 'iva', 'discounts', 'value']