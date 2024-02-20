from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

# Modelos
from billing.models import BillingModel

# Formularios
from billing.forms import BillingForm

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