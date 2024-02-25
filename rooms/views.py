from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

# Security
from django.contrib.auth.decorators import login_required

# Modelos 
from rooms.models import RoomsModel
from rooms.models import TypesModel
from rooms.models import StatusModel

# Forms
from rooms.forms import RoomForm

# Vistas 

## Rooms 
@login_required
def rooms(request):
    # Verificamos si es POST y si el formulario esta correcto
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms')

    # Cargamos los filtros
    status_filter = request.GET.get('status')
    types_filter = request.GET.get('type')

    items = RoomsModel.objects.select_related('status', 'types').all().order_by('number')
    status = StatusModel.objects.all()
    types = TypesModel.objects.all()

    if status_filter: items = items.filter(status__name__icontains=status_filter)
    if types_filter: items = items.filter(types__id=types_filter)

    # Formulario
    form = RoomForm()

    return render(request, 'rooms.html', {
        'form': form,
        'items': items,
        'types': types,
        'status': status
    })

@login_required
def rooms_delete(request, id_room:int):
    room = get_object_or_404(RoomsModel, pk=id_room)
    room.delete()
    return redirect('rooms')

@login_required
def rooms_update(request, id_room:int):
    room = get_object_or_404(RoomsModel, pk=id_room)
    
    # POST
    if request.method == 'POST':
        # Llenar con la información del cliente
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('rooms')
        
    # GET
    if request.method == 'GET':
        form = RoomForm(instance=room)

    return render(request, 'rooms_update.html', {
        'form': form, 
        'room': room
    })