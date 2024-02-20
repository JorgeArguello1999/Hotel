from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

# Modelos
from billing.models import BillingModel

# Formularios
from billing.forms import BillingForm

# Funciones
from main.functions import calculate_price_of_room

# Vistas
def billing(request):
    # GET 
    if request.method == 'GET':
        form = BillingForm()
        items = BillingModel.objects.all()
        return render(request, 'billing.html', {
            'form': form,
            'items': items
        })
    
    # POST
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            # Obteniendo el precio a pagar
            data_client = form.instance.client # Obligatorio

            # Pueden tener o no un valor
            try: data_iva = form.instance.iva.price 
            except: data_iva = 0

            try: data_discount = form.instance.discounts.price
            except: data_discount = 0

            data_iva = data_iva if data_iva is not None else 0
            data_discount = data_discount if data_discount is not None else 0

            value = calculate_price_of_room(
                data=[
                    data_client.adults if data_client.adults is not None else 0,
                    data_client.childrens if data_client.childrens is not None else 0,
                    data_client.third_age if data_client.third_age is not None else 0
                ], 
                iva=data_iva, 
                discount=data_discount
            )

            form.instance.value = value
            form.save()

            return redirect('billing')
        else:
            return redirect('billing')

def billing_update(request, id_billing):
    return redirect('billing')

def billing_delete(request, id_billing):
    item = get_object_or_404(BillingModel, pk=id_billing)
    item.delete()
    return redirect('billing')