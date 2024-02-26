from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Security
from django.contrib.auth.decorators import login_required

# Modelos
from clients.models import ClientsModel

# Formularios
from clients.forms import ClientForm

@login_required
def clients(request):
    form = ClientForm() 
    items = ClientsModel.objects.all().order_by('cedula')

    # Filtros
    search_query = request.GET.get('search_query')
    if search_query: 
        items = items.filter(cedula__icontains=search_query)

    return render(request, 'clients.html', {
        'form': form,
        'items': items
    })
    
    # POST
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients')

@login_required
def clients_update(request, id_client):
    client = get_object_or_404(ClientsModel, pk=id_client)
    
    # POST
    if request.method == 'POST':
        # Llenar con la información del cliente
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients')
        
    # GET
    if request.method == 'GET':
        form = ClientForm(instance=client)

    return render(request, 'clients_update.html', {
        'form': form, 
        'client': client
    })

@login_required
def clients_delete(request, id_client):
    client = get_object_or_404(ClientsModel, pk=id_client)
    client.delete()
    return redirect('clients')