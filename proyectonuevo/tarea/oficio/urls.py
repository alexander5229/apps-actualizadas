
from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Aprendices
    path('aprendices/', views.lista_aprendices, name='lista_aprendices'),
    path('aprendices/nuevo/', views.crear_aprendiz, name='crear_aprendiz'),
    path('aprendices/editar/<int:id>/', views.editar_aprendiz, name='editar_aprendiz'),
    path('aprendices/eliminar/<int:id>/', views.eliminar_aprendiz, name='eliminar_aprendiz'),

    # Programas
    path('programas/', views.lista_programas, name='lista_programas'),
    path('programas/nuevo/', views.crear_programa, name='crear_programa'),
    path('programas/editar/<int:id>/', views.editar_programa, name='editar_programa'),
    path('programas/eliminar/<int:id>/', views.eliminar_programa, name='eliminar_programa'),

    # Instructores
    path('instructores/', views.lista_instructores, name='lista_instructores'),
    path('instructores/nuevo/', views.crear_instructor, name='crear_instructor'),
    path('instructores/editar/<int:id>/', views.editar_instructor, name='editar_instructor'),
    path('instructores/eliminar/<int:id>/', views.eliminar_instructor, name='eliminar_instructor'),

    # Competencias
    path('competencias/', views.lista_competencias, name='lista_competencias'),
    path('competencias/nuevo/', views.crear_competencia, name='crear_competencia'),
    path('competencias/editar/<int:id>/', views.editar_competencia, name='editar_competencia'),
    path('competencias/eliminar/<int:id>/', views.eliminar_competencia, name='eliminar_competencia'),

    # Locales y mapa
    path('locales/', views.lista_locales, name='lista_locales'),
    path('locales/nuevo/', views.crear_local, name='crear_local'),
    path('locales/editar/<int:id>/', views.editar_local, name='editar_local'),
    path('locales/eliminar/<int:id>/', views.eliminar_local, name='eliminar_local'),
    path('mapa/', views.mapa_view, name='mapa_view'),
    path('api/guardar-direccion/', views.guardar_direccion, name='guardar_direccion'),
]