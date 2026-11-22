from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='reserva/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.inicio, name='inicio'),
    path('clientes/', views.listar_clientes, name='lista_clientes'),
    path('clientes/nuevo/', views.crear_cliente, name='crear_cliente'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('parqueadero/', views.listar_parqueadero, name='lista_parqueadero'),
    path('parqueadero/nuevo/', views.crear_parqueadero, name='crear_parqueadero'),
    path('parqueadero/editar/<int:pk>/', views.editar_parqueadero, name='editar_parqueadero'),
    path('parqueadero/eliminar/<int:pk>/', views.eliminar_parqueadero, name='eliminar_parqueadero'),
    path('modulo/', views.listar_modulo, name='lista_modulo'),
    path('modulo/nuevo/', views.crear_modulo, name='crear_modulo'),
    path('modulo/editar/<int:pk>/', views.editar_modulo, name='editar_modulo'),
    path('modulo/eliminar/<int:pk>/', views.eliminar_modulo, name='eliminar_modulo'),
    path('reserva/', views.listar_reserva, name='lista_reserva'),
    path('reserva/nuevo/', views.crear_reserva, name='crear_reserva'),
    path('reserva/editar/<int:pk>/', views.editar_reserva, name='editar_reserva'),
    path('reserva/eliminar/<int:pk>/', views.eliminar_reserva, name='eliminar_reserva'),
    path("mapa/", views.mapa_view, name="mapa"),
    path("mapa/guardar/", views.guardar_direccion, name="guardar_direccion"),

]