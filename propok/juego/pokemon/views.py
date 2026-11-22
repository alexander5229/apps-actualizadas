
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DireccionBuscada
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST
from .models import Entrenadores, Pokemones, Gimnasio
from .forms import (EntrenadoresForm,PokemonesForm,GimnasioForm)
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings



# ---------------------------------------------------------------------------
# Autenticación
# ---------------------------------------------------------------------------

def login_view(request):
    # Si ya está autenticado, no tiene sentido mostrar el login
    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())

            # Respeta ?next=... solo si es una URL segura
            siguiente = request.GET.get('next')
            if siguiente and url_has_allowed_host_and_scheme(
                siguiente, allowed_hosts={request.get_host()}
            ):
                return redirect(siguiente)
            return redirect('inicio')
    else:
        form = AuthenticationForm()

    return render(request, 'pokemon/login.html', {'form': form})


@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')


# ==================================
# CRUD ENTRENADORES
# ==================================

# READ: listar entrenadores
@login_required
def listar_entrenadores(request):
    query = request.GET.get('q', '')

    if query:
        # Filtra si coincide el nombre, el apellido o el documento
        entrenadores = Entrenadores.objects.filter(
            Q(nombre__icontains=query) | 
            Q(apellido__icontains=query) | 
            Q(documento__icontains=query)
        )
    else:
        entrenadores = Entrenadores.objects.all()

    return render(request,'pokemon/listar_entrenadores.html',{'entrenadores': entrenadores, 'query': query})

# CREATE: registrar entrenador
@login_required
@permission_required('pokemon.add_entrenador', raise_exception=True)
def crear_entrenador(request):

    if request.method == 'POST':

        formulario = EntrenadoresForm(request.POST,request.FILES)

        if formulario.is_valid():

            formulario.save()

            return redirect('listar_entrenadores')

    else:

        formulario = EntrenadoresForm()

    return render(request,'pokemon/formulario_entrenador.html',{'formulario': formulario})

# UPDATE: editar entrenador
@login_required
@permission_required('pokemon.change_entrenador', raise_exception=True)
def editar_entrenador(request, id):

    entrenador = get_object_or_404(Entrenadores,id=id)

    if request.method == 'POST':

        formulario = EntrenadoresForm(request.POST,request.FILES,instance=entrenador)

        if formulario.is_valid():

            formulario.save()

            return redirect('listar_entrenadores')

    else:

        formulario = EntrenadoresForm(
            instance=entrenador
        )

    return render(
        request,
        'pokemon/formulario_entrenador.html',
        {
            'formulario': formulario,
            'entrenador': entrenador
        }
    )


# DELETE: eliminar entrenador
@login_required
@permission_required('pokemon.delete_entrenador', raise_exception=True)
def eliminar_entrenador(request, id):

    entrenador = get_object_or_404(
        Entrenadores,
        id=id
    )

    if request.method == 'POST':

        entrenador.delete()

        return redirect('listar_entrenadores')

    return render(
        request,
        'pokemon/eliminar_entrenador.html',
        {'entrenador': entrenador}
    )

# READ: listar pokemones
@login_required
def listar_pokemones(request):

    query = request.GET.get('q', '')
    
    if query:
            # Filtra si coincide el nombre
        pokemones = Pokemones.objects.filter(
            Q(nombre__icontains=query) 
            
            )
    else:
        pokemones = Pokemones.objects.all()


    return render(
        request,
        'pokemon/listar_pokemones.html',
        {'pokemones': pokemones, 'query': query}
    )


# CREAR: Listar pokemones

# CREATE: registrar pokemon
@login_required
@permission_required('pokemon.add_pokemones', raise_exception=True)
def crear_pokemon(request):

    if request.method == 'POST':

        formulario = PokemonesForm(
            request.POST,
            request.FILES
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_pokemones')

    else:
        formulario = PokemonesForm()

    return render(
        request,
        'pokemon/formulario_pokemon.html',
        {'formulario': formulario}
    )

# UPDATE: editar pokemon
@login_required
@permission_required('pokemon.change_pokemones', raise_exception=True)
def editar_pokemon(request, id):

    pokemon = get_object_or_404(Pokemones, id=id)

    if request.method == 'POST':

        formulario = PokemonesForm(
            request.POST,
            request.FILES,
            instance=pokemon
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_pokemones')

    else:
        formulario = PokemonesForm(instance=pokemon)

    return render(
        request,
        'pokemon/formulario_pokemon.html',
        {
            'formulario': formulario,
            'pokemon': pokemon
        }
    )


# DELETE: eliminar pokemon
@login_required
@permission_required('pokemon.delete_pokemones', raise_exception=True)
def eliminar_pokemon(request, id):

    pokemon = get_object_or_404(Pokemones, id=id)

    if request.method == 'POST':

        pokemon.delete()

        return redirect('listar_pokemones')

    return render(
        request,
        'pokemon/eliminar_pokemon.html',
        {'pokemon': pokemon}
    )

# READ: listar gimnasios
@login_required
def listar_gimnasios(request):

    query = request.GET.get('q', '')
    
    if query:
        # Filtra si coincide el lider, elemento o medallas
        gimnasios = Gimnasio.objects.filter(
            Q(lider_gim__icontains=query) | 
            Q(elemento_gim__icontains=query) |
            Q(medallas__icontains=query)
        )
    else:
        gimnasios = Gimnasio.objects.all()

    return render(
        request,
        'pokemon/listar_gimnasios.html',
        {'gimnasios': gimnasios, 'query': query}
    )

# CREATE: registrar gimnasio
@login_required
@permission_required('pokemon.add_gimnasio', raise_exception=True)
def crear_gimnasio(request):

    if request.method == 'POST':

        formulario = GimnasioForm(
            request.POST,
            request.FILES
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_gimnasios')

    else:
        formulario = GimnasioForm()

    return render(
        request,
        'pokemon/formulario_gimnasio.html',
        {'formulario': formulario}
    )

# UPDATE: editar gimnasio
@login_required
@permission_required('pokemon.change_gimnasio', raise_exception=True)
def editar_gimnasio(request, id):

    gimnasio = get_object_or_404(Gimnasio, id=id)

    if request.method == 'POST':

        formulario = GimnasioForm(
            request.POST,
            request.FILES,
            instance=gimnasio
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_gimnasios')

    else:
        formulario = GimnasioForm(instance=gimnasio)

    return render(
        request,
        'pokemon/formulario_gimnasio.html',
        {
            'formulario': formulario,
            'gimnasio': gimnasio
        }
    )

# DELETE: eliminar gimnasio
@login_required
@permission_required('pokemon.delete_gimnasio', raise_exception=True)
def eliminar_gimnasio(request, id):

    gimnasio = get_object_or_404(Gimnasio, id=id)

    if request.method == 'POST':

        gimnasio.delete()

        return redirect('listar_gimnasios')

    return render(
        request,
        'pokemon/eliminar_gimnasio.html',
        {'gimnasio': gimnasio}
    )

# ERROR 403
def error_403(request, exception=None):
    return render(request, 'pokemon/403.html', status=403)


# INICIO: pagina principal de ProPok
def inicio(request):

    return render(
        request,
        'pokemon/inicio.html'
    )


#Vista para consultar direcciones
from django.shortcuts import render

def mapa_view(request):
    return render(request, 'pokemon/mapa.html') # Asegúrate de que coincida con el nombre de tu archivo html


@csrf_exempt # forma temporal para simplificar peticiones AJAX en proyectos académicos
def guardar_direccion(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            direccion = data.get('address')
            lat = data.get('lat')
            lon = data.get('lon')

            if direccion:
                # Guardar en PostgreSQL
                DireccionBuscada.objects.create(
                    direccion=direccion,
                    latitud=lat,
                    longitud=lon
                )
                return JsonResponse({"status": "success", "message": "¡Guardado en PostgreSQL con éxito!"})
            else:
                return JsonResponse({"status": "error", "message": "Dirección vacía"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
            
    return JsonResponse({"status": "error", "message": "Método no permitido"}, status=405)