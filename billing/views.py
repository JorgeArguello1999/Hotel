from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

# Modelos
from billing.models import BillingModel

# Formularios
from billing.forms import BillingForm

# Funciones
from main.functions import calculate_price_of_room
from main.functions import update_reservation_status
from main.functions import update_room_status

# Security
from django.contrib.auth.decorators import login_required

# Vistas
@login_required
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
                discount=data_discount,
                date_in=form.instance.client.entry_date,
                date_out=form.instance.client.out_date
            )

            form.instance.value = value

            # Actualizamos el estado de la reservación
            update_reservation_status(form.instance.client.id, False)
            update_room_status(form.instance.client, 'Limpiar')

            # Guardamos la información
            form.save()

            return redirect('billing')
        else:
            return redirect('billing')

@login_required
def billing_delete(request, id_billing):
    item = get_object_or_404(BillingModel, pk=id_billing)
    item.delete()

    # Actualizamos los estados de la habitación
    update_reservation_status(item.client.id, True)
    update_room_status(item.client, 'Ocupado')

    return redirect('billing')