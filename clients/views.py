from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Modelos
from clients.models import ClientsModel

# Formularios
from clients.forms import ClientForm

def clients(request):
    # GET
    if request.method == 'GET':
        form = ClientForm() 
        items = ClientsModel.objects.all().order_by('cedula')
        return render(request, 'clients.html', {
            'form': form,
            'items': items
        })
    
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients')

def clients_update(request, id_client):
    # Obtener el cliente que se va a actualizar
    client = get_object_or_404(ClientsModel, pk=id_client)
    
    # Si la solicitud es POST, procesar el formulario
    if request.method == 'POST':
        # Llenar el formulario con los datos del cliente y los datos enviados en la solicitud
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients')
    else:
        form = ClientForm(instance=client)

    # Renderizar la plantilla con el formulario y el cliente
    return render(request, 'clients_update.html', {'form': form, 'client': client})

def clients_delete(request, id_client):
    client = get_object_or_404(ClientsModel, pk=id_client)
    client.delete()
    return redirect('clients')