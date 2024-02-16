from django.shortcuts import render
from django.shortcuts import redirect

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
            return redirect('rooms')
        else:
            print('Form NOT VALID')
    
    return render(request, 'rooms.html', {
        'form': form,
        'lista': lista
    })

def rooms_update(request, id_habitacion):
    return redirect('rooms') 

def rooms_delete(request, id_habitacion):
    try:
        # Buscar la habitación por su ID
        habitacion = habitaciones.objects.get(pk=id_habitacion)
        # Eliminar la habitación
        habitacion.delete()
    except Exception as e:
        print(e)

    return redirect('rooms')