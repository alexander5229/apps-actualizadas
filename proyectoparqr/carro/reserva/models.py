from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Cliente(models.Model):
    
    nombre = models.CharField(max_length=50)
    documento = models.CharField(max_length=15, unique=True)
    tipo_documento = models.CharField(max_length=10)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True) 

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Doc: {self.documento}"
    
class Parqueadero(models.Model):
    
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    descripcion = models.TextField()
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=50)
    capacidad = models.IntegerField() 

    def __str__(self):
        return self.nombre

class Modulo(models.Model):

    parqueadero = models.ForeignKey(Parqueadero, on_delete=models.CASCADE, related_name='modulos')
    color = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    

    def __str__(self):
        return f"{self.tipo} - {self.parqueadero.nombre}"
    
class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    parqueadero = models.ForeignKey(Parqueadero, on_delete=models.CASCADE, related_name='reservas')
    modulo = models.ForeignKey(Modulo, on_delete=models.SET_NULL, null=True,blank=True, related_name='reservas')

    # fecha_creacion = models.DateField(auto_now_add=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.cliente.nombre} - {self.parqueadero.nombre}"
    


class Direccion(models.Model):
  usuario = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.SET_NULL,
      null=True,
      blank=True,
      related_name="direcciones",
  )
  direccion = models.CharField(max_length=255)
  latitud = models.DecimalField(max_digits=9, decimal_places=6)
  longitud = models.DecimalField(max_digits=9, decimal_places=6)
  creado_en = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = "Dirección"
    verbose_name_plural = "Direcciones"
    ordering = ["-creado_en"]

  def __str__(self):
    return self.direccion