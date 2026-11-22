import json
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Aprendiz, Local,Competencias,DireccionBuscada,Instructores,Programa
from .forms import AprendizForm,CompetenciasForm,InstructoresForm,LocalForm,ProgramaForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def inicio(request):
    return render(request, 'oficio/inicio.html')
# Administracion de permisos
def login_view(request):
    # Si ya está autenticado, no tiene sentido mostrar el login
    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bienvenido, {user.username}.')
            next_url = request.POST.get('next') or request.GET.get('next') or 'inicio'
            return redirect(next_url)
        messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm(request)

    return render(request, 'oficio/login.html', {'form': form})


@require_POST
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada correctamente.')
    return redirect('login')


@login_required
def lista_aprendices(request):
    query = request.GET.get('q', '')

    if query:
        # Filtra si coincide el nombre, el apellido o el documento
        aprendices = Aprendiz.objects.filter(
            Q(nombre__icontains=query) | 
            Q(apellido__icontains=query) | 
            Q(documento__icontains=query)
        )
    else:

        aprendices = Aprendiz.objects.all()


    return render(
        request,
        "oficio/lista_aprendices.html",{
        'aprendices': aprendices, 'query': query}
    )


# CREATE: Registrar un nuevo aprendiz
@login_required
@permission_required('oficio.add_aprendiz', raise_exception=True)
def crear_aprendiz(request):

    if request.method == 'POST':

        formulario = AprendizForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_aprendices')

    else:
        formulario = AprendizForm()

    contexto = {
        'formulario': formulario
    }

    return render(
        request,
        'oficio/crear_aprendiz.html',
        contexto
    )


@login_required
@permission_required('oficio.change_aprendiz', raise_exception=True)
def editar_aprendiz(request, id):
    aprendiz = get_object_or_404(Aprendiz, id=id)

    if request.method == 'POST':
        formulario = AprendizForm(request.POST, instance=aprendiz)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_aprendices')
    else:
        formulario = AprendizForm(instance=aprendiz)

    return render(request, 'oficio/crear_aprendiz.html', {
        'formulario': formulario,
        'titulo': 'Editar aprendiz'
    })


# DELETE: Eliminar aprendiz
@login_required
@permission_required('oficio.delete_aprendiz', raise_exception=True)
def eliminar_aprendiz(request, id):
    aprendiz = get_object_or_404(Aprendiz, id=id)

    if request.method == 'POST':
        aprendiz.delete()
        return redirect('lista_aprendices')

    return render(request, 'oficio/eliminar_aprendiz.html', {
        'aprendiz': aprendiz
    })


@login_required
def lista_programas(request):
    query = request.GET.get('q', '')
    if query:
        programas = Programa.objects.filter(
            Q(nombre__icontains=query)
            | Q(ficha__icontains=query)
            | Q(jornada__icontains=query)
        )
    else:
        programas = Programa.objects.all()

    return render(
        request,
        'oficio/lista_programas.html',
        {'programas': programas, 'query': query},
    )

@login_required
@permission_required('oficio.add_programa', raise_exception=True)
def crear_programa(request):
    if request.method == 'POST':
        formulario = ProgramaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Programa registrado correctamente.')
            return redirect('lista_programas')
    else:
        formulario = ProgramaForm()

    return render(request, 'oficio/form_programa.html', {'formulario': formulario})

@login_required
@permission_required('oficio.change_programa', raise_exception=True)
def editar_programa(request, id):
    programa = get_object_or_404(Programa, id=id)
    if request.method == 'POST':
        formulario = ProgramaForm(request.POST, instance=programa)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Programa actualizado correctamente.')
            return redirect('lista_programas')
    else:
        formulario = ProgramaForm(instance=programa)

    return render(
        request,
        'oficio/form_programa.html',
        {'formulario': formulario, 'titulo': 'Editar programa'},
    )

@login_required
@permission_required('oficio.delete_programa', raise_exception=True)
def eliminar_programa(request, id):
    programa = get_object_or_404(Programa, id=id)
    if request.method == 'POST':
        programa.delete()
        messages.success(request, 'Programa eliminado correctamente.')
        return redirect('lista_programas')

    return render(request, 'oficio/eliminar_programa.html', {'programa': programa})


# --- INSTRUCTORES ---
@login_required
def lista_instructores(request):
    query = request.GET.get('q', '')
    if query:
        instructores = Instructores.objects.filter(
            Q(nombre__icontains=query)
            | Q(apellido__icontains=query)
            | Q(documento__icontains=query)
            | Q(especialidad__icontains=query)
        )
    else:
        instructores = Instructores.objects.all()

    return render(
        request,
        'oficio/lista_instructores.html',
        {'instructores': instructores, 'query': query},
    )

@login_required
@permission_required('oficio.add_instructor', raise_exception=True)
def crear_instructor(request):
    if request.method == 'POST':
        formulario = InstructoresForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Instructor registrado correctamente.')
            return redirect('lista_instructores')
    else:
        formulario = InstructoresForm()

    return render(request, 'oficio/form_instructor.html', {'formulario': formulario})


@login_required
@permission_required('oficio.change_instructor', raise_exception=True)
def editar_instructor(request, id):
    instructor = get_object_or_404(Instructores, id=id)
    if request.method == 'POST':
        formulario = InstructoresForm(request.POST, instance=instructor)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Instructor actualizado correctamente.')
            return redirect('lista_instructores')
    else:
        formulario = InstructoresForm(instance=instructor)

    return render(
        request,
        'oficio/form_instructor.html',
        {'formulario': formulario, 'titulo': 'Editar instructor'},
    )


@login_required
@permission_required('oficio.delete_instructor', raise_exception=True)
def eliminar_instructor(request, id):
    instructor = get_object_or_404(Instructores, id=id)
    if request.method == 'POST':
        instructor.delete()
        messages.success(request, 'Instructor eliminado correctamente.')
        return redirect('lista_instructores')

    return render(
        request,
        'oficio/eliminar_instructor.html',
        {'instructor': instructor},
    )


# --- COMPETENCIAS ---
@login_required
def lista_competencias(request):
    query = request.GET.get('q', '')
    if query:
        competencias = Competencias.objects.filter(
            Q(nombre__icontains=query)
            | Q(ficha__icontains=query)
            | Q(instructores__icontains=query)
        )
    else:
        competencias = Competencias.objects.all()

    return render(
        request,
        'oficio/lista_competencias.html',
        {'competencias': competencias, 'query': query},
    )


@login_required
@permission_required('oficio.add_competencia', raise_exception=True)
def crear_competencia(request):
    if request.method == 'POST':
        formulario = CompetenciasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Competencia registrada correctamente.')
            return redirect('lista_competencias')
    else:
        formulario = CompetenciasForm()

    return render(request, 'oficio/form_competencia.html', {'formulario': formulario})


@login_required
@permission_required('oficio.change_competencia', raise_exception=True)
def editar_competencia(request, id):
    competencia = get_object_or_404(Competencias, id=id)
    if request.method == 'POST':
        formulario = CompetenciasForm(request.POST, instance=competencia)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Competencia actualizada correctamente.')
            return redirect('lista_competencias')
    else:
        formulario = CompetenciasForm(instance=competencia)

    return render(
        request,
        'oficio/form_competencia.html',
        {'formulario': formulario, 'titulo': 'Editar competencia'},
    )


@login_required
@permission_required('oficio.delete_competencia', raise_exception=True)
def eliminar_competencia(request, id):
    competencia = get_object_or_404(Competencias, id=id)
    if request.method == 'POST':
        competencia.delete()
        messages.success(request, 'Competencia eliminada correctamente.')
        return redirect('lista_competencias')

    return render(
        request,
        'oficio/eliminar_competencia.html',
        {'competencia': competencia},
    )


# --- LOCALES Y MAPA ---
@login_required
def lista_locales(request):
    query = request.GET.get('q', '')
    if query:
        locales = Local.objects.filter(
            Q(nombre__icontains=query) | Q(direccion__icontains=query)
        )
    else:
        locales = Local.objects.all()

    return render(
        request,
        'oficio/lista_locales.html',
        {'locales': locales, 'query': query},
    )


@login_required
@permission_required('oficio.add_local', raise_exception=True)
def crear_local(request):
    if request.method == 'POST':
        formulario = LocalForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Local registrado correctamente.')
            return redirect('lista_locales')
    else:
        formulario = LocalForm()

    return render(request, 'oficio/form_local.html', {'formulario': formulario})


@login_required
@permission_required('oficio.change_local', raise_exception=True)
def editar_local(request, id):
    local = get_object_or_404(Local, id=id)
    if request.method == 'POST':
        formulario = LocalForm(request.POST, instance=local)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Local actualizado correctamente.')
            return redirect('lista_locales')
    else:
        formulario = LocalForm(instance=local)

    return render(
        request,
        'oficio/form_local.html',
        {'formulario': formulario, 'titulo': 'Editar local'},
    )


@login_required
@permission_required('oficio.delete_local', raise_exception=True)
def eliminar_local(request, id):
    local = get_object_or_404(Local, id=id)
    if request.method == 'POST':
        local.delete()
        messages.success(request, 'Local eliminado correctamente.')
        return redirect('mapa_view')

    return render(request, 'oficio/eliminar_local.html', {'local': local})


def mapa_view(request):
    locales = Local.objects.all()
    return render(request, 'oficio/mapa.html') 


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

