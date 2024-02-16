from django.shortcuts import render
# Formulario
from rooms.forms import HabitacionForm
# Modelo
from rooms.models import habitaciones

# Vistas para Habitaciones
def rooms(request):

    # Formulario
    form = HabitacionForm()

    # Lista de habitaciones
    lista = habitaciones.objects.select_related('estado', 'tipo').all()
    
    if request.method == 'POST':
        form = HabitacionForm(request.POST)
        if form.is_valid():
            form.save()
    
    if request.method == 'UPDATE':
        # logica para actualizar los cuartos
        pass

    return render(request, 'rooms.html', {
        'form': form,
        'lista': lista
    })