from django.contrib import admin
from .models import Aprendiz, Programa, Instructores, Competencias,BusquedaUbicacion,DireccionBuscada, Local
# Register your models here.

@admin.register(Aprendiz)
class AprendizAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'documento', 'tipo_documento', 'correo', 'ficha', 'Programa')
    search_fields = ('nombre', 'apellido', 'documento', 'correo')


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ficha', 'jornada', 'modalidad', 'nivel_profesional', 'Instructores')
    search_fields = ('nombre', 'ficha')


@admin.register(Instructores)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'documento', 'especialidad', 'ficha_asignada', 'correo')
    search_fields = ('nombre', 'apellido', 'documento', 'especialidad')


@admin.register(Competencias)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ficha', 'instructores')
    search_fields = ('nombre', 'ficha', 'instructores')


@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'lat', 'lng')
    search_fields = ('nombre', 'direccion')


@admin.register(BusquedaUbicacion)
class BusquedaUbicacionAdmin(admin.ModelAdmin):
    list_display = ('direccion', 'fecha_busqueda')


@admin.register(DireccionBuscada)
class DireccionBuscadaAdmin(admin.ModelAdmin):
    list_display = ('direccion', 'latitud', 'longitud', 'fecha_busqueda')


# @admin.register(Perfil)
# class PerfilAdmin(admin.ModelAdmin):
#     list_display = ('usuario', 'rol_principal', 'telefono')
#     list_filter = ('rol_principal',)