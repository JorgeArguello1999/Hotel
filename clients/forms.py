from django import forms

# Modelos 
from clients.models import ClientsModel

class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientsModel
        fields = '__all__'
