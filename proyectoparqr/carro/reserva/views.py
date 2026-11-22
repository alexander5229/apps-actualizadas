
from decimal import Decimal, InvalidOperation
import json
from django.shortcuts import render
from .forms import ClienteForm
from .models import Cliente
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
# from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST
from .models import Cliente,Parqueadero,Modulo,Reserva
from .forms import (ClienteForm, ParqueaderoForm, ModuloForm, ReservaForm)
from .models import Direccion
from django.conf import settings




# Create your views here.

# PAGINA DE INICIO
@login_required
def inicio(request):
    return render(request, 'reserva/inicio.html')


# CRUD CLIENTES
# READ
@login_required
def listar_clientes(request): 
    query = request.GET.get('q', '')

    if query:
        # Filtra si coincide el nombre, el apellido o el documento
        clientes = Cliente.objects.filter(
            Q(nombre__icontains=query) | 
            Q(apellido__icontains=query) | 
            Q(documento__icontains=query)
        )
    else:
        clientes = Cliente.objects.all()

    return render(request,'reserva/lista_clientes.html',{'clientes': clientes, 'query': query})

 
# CREATE
@login_required
@permission_required('reserva.add_cliente', raise_exception=True)
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente Registrado')
            return redirect('lista_clientes')
    else:
            form = ClienteForm()
    return render(request,'reserva/form_cliente.html', {'form': form, 'accion': 'Registrar'})

# UPDATE
@login_required
@permission_required('reserva.change_cliente', raise_exception=True)
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Datos del cliente actualizados correctamente!')
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
        
    return render(request, 'reserva/form_cliente.html', {'form': form, 'accion': 'Actualizar'})

# DELETE
@login_required
@permission_required('reserva.delete_cliente', raise_exception=True)
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        
        cliente.delete()
        messages.error(request, 'El cliente ha sido eliminado')
        return redirect('lista_clientes')
        
    return render(request, 'reserva/eliminar_cliente.html', {'cliente': cliente})


# CRUD MODULO
# READ
@login_required
def listar_modulo(request): 
    query = request.GET.get('q', '')

    if query:
        # Filtra si coincide el nombre, el apellido o el documento
        modulo = Modulo.objects.filter(
            Q(color__icontains=query) | 
            Q(tipo__icontains=query) | 
            Q(estado__icontains=query)
        )
    else:
        modulos = Modulo.objects.all()

    return render(request,'reserva/lista_modulo.html',{'modulos': modulos, 'query': query})

 
# CREATE
@login_required
@permission_required('reserva.add_modulo', raise_exception=True)
def crear_modulo(request):
    if request.method == 'POST':
        form = ModuloForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modulo Registrado')
            return redirect('lista_modulo')
    else:
            form = ModuloForm()
    return render(request,'reserva/form_modulo.html', {'form': form, 'accion': 'Registrar'})

# UPDATE
@login_required
@permission_required('reserva.change_modulo', raise_exception=True)
def editar_modulo(request, pk):
    modulo = get_object_or_404(Modulo, pk=pk)
    if request.method == 'POST':
        form = ModuloForm(request.POST, instance=modulo)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Datos del modulo actualizados correctamente!')
            return redirect('lista_modulo')
    else:
        form = ModuloForm(instance=modulo)
        
    return render(request, 'reserva/form_modulo.html', {'form': form, 'accion': 'Actualizar'})

# DELETE
@login_required
@permission_required('reserva.delete_modulo', raise_exception=True)
def eliminar_modulo(request, pk):
    modulo = get_object_or_404(Modulo, pk=pk)
    if request.method == 'POST':
        
        modulo.delete()
        messages.error(request, 'El modulo ha sido eliminado')
        return redirect('lista_modulo')
        
    return render(request, 'reserva/eliminar_modulo.html', {'modulo': modulo})

@login_required
def listar_parqueadero(request): 
    query = request.GET.get('q', '')

    if query:
        # Filtra si coincide el nombre, el apellido o el documento
        parqueaderos = Parqueadero.objects.filter(
            Q(nombre__icontains=query)
        )
    else:
        parqueaderos = Parqueadero.objects.all()

    return render(request,'reserva/lista_parqueadero.html',{'parqueaderos': parqueaderos, 'query': query})

 
# CREATE
@login_required
@permission_required('reserva.add_parqueadero', raise_exception=True)
def crear_parqueadero(request):
    if request.method == 'POST':
        form = ParqueaderoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Parqueadero Registrado')
            return redirect('lista_parqueadero')
    else:
            form = ParqueaderoForm()
    return render(request,'reserva/form_parqueadero.html', {'form': form, 'accion': 'Registrar'})

# UPDATE
@login_required
@permission_required('reserva.change_parqueadero', raise_exception=True)
def editar_parqueadero(request, pk):
    parqueadero = get_object_or_404(Parqueadero, pk=pk)
    if request.method == 'POST':
        form = ParqueaderoForm(request.POST, instance=parqueadero)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Datos del parqueadero actualizados correctamente!')
            return redirect('lista_parqueadero')
    else:
        form = ParqueaderoForm(instance=parqueadero)
        
    return render(request, 'reserva/form_parqueadero.html', {'form': form, 'accion': 'Actualizar'})

# DELETE
@login_required
@permission_required('reserva.delete_parqueadero', raise_exception=True)
def eliminar_parqueadero(request, pk):
    parqueadero = get_object_or_404(Parqueadero, pk=pk)
    if request.method == 'POST':
        
        parqueadero.delete()
        messages.error(request, 'El parqueadero ha sido eliminado')
        return redirect('lista_parqueadero')
        
    return render(request, 'reserva/eliminar_parqueadero.html', {'parqueadero': parqueadero})


# CRUD RESERVA
# READ
@login_required
def listar_reserva(request): 
    query = request.GET.get('q', '')

    if query:
        # Filtra si coincide el nombre, el apellido o el documento
        reservas = Reserva.objects.filter(
            Q(modulo__color__icontains=query) |
            Q(modulo__tipo__icontains=query)
        )
    else:
        reservas = Reserva.objects.all()

    return render(request,'reserva/lista_reserva.html',{'reservas': reservas, 'query': query})

 
# CREATE
@login_required
@permission_required('reserva.add_reserva', raise_exception=True)
def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reserva Registrada')
            return redirect('lista_reserva')
    else:
            form = ReservaForm()
    return render(request,'reserva/form_reserva.html', {'form': form, 'accion': 'Registrar'})

# UPDATE
@login_required
@permission_required('reserva.change_reserva', raise_exception=True)
def editar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Datos de la reserva actualizados correctamente!')
            return redirect('lista_reserva')
    else:
        form = ReservaForm(instance=reserva)
        
    return render(request, 'reserva/form_reserva.html', {'form': form, 'accion': 'Actualizar'})

# DELETE
@login_required
@permission_required('reserva.delete_reserva', raise_exception=True)
def eliminar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        
        reserva.delete()
        messages.error(request, 'La reserva ha sido eliminada')
        return redirect('lista_reserva')
        
    return render(request, 'reserva/eliminar_reserva.html', {'reserva': reserva})


def error_403(request, exeption=None):
    return render(request, "403.html", status=403)




@login_required
def mapa_view(request):
  return render(request, "reserva/mapa.html")


@login_required
@require_POST
def guardar_direccion(request):
  try:
    data = json.loads(request.body.decode("utf-8"))
    address = str(data.get("address", "")).strip()
    lat = data.get("lat")
    lon = data.get("lon")

    if not address or lat is None or lon is None:
      return JsonResponse(
          {"message": "Faltan datos de dirección o coordenadas."},
          status=400,
      )

    try:
      lat_dec = Decimal(str(lat))
      lon_dec = Decimal(str(lon))
    except InvalidOperation:
      return JsonResponse(
          {"message": "Coordenadas no válidas."},
          status=400,
      )

    Direccion.objects.create(
        usuario=request.user,
        direccion=address[:255],
        latitud=lat_dec,
        longitud=lon_dec,
    )

    return JsonResponse({
        "message": "Dirección guardada en la base de datos.",
        "lat": str(lat_dec),
        "lon": str(lon_dec),
    })
  except json.JSONDecodeError:
    return JsonResponse({"message": "JSON inválido."}, status=400)
