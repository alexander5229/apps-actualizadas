from django.contrib import admin
from .models import Cliente,Parqueadero,Modulo,Reserva

# Register your models here.

#

admin.site.register(Cliente)
admin.site.register(Parqueadero)
admin.site.register(Modulo)
admin.site.register(Reserva)