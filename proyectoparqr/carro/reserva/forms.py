from django import forms
from .models import Cliente,Parqueadero,Modulo,Reserva

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','apellido','tipo_documento','documento','correo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej:luis'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej:perez'}),
            'tipo_documento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej:c.c'}),
            'documento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej:12345'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ej:luisperez@gmail.com'}),

        }

class ParqueaderoForm(forms.ModelForm):
    class Meta:
        model = Parqueadero
        fields = ['nombre','ubicacion','descripcion','correo','telefono','capacidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }    

class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ['color','tipo','estado', 'parqueadero']
        widgets = {
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'parqueadero': forms.Select(attrs={'class': 'form-select'}),
        }


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'parqueadero', 'modulo', 'fecha_inicio','fecha_fin','estado']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'parqueadero': forms.Select(attrs={'class': 'form-select'}),
            'modulo': forms.Select(attrs={'class': 'form-select'}),
            # 'fecha_creacion': forms.DateInput(attrs={'class': 'form-control', 'type':'date-local'}),
            'fecha_inicio': forms.DateTimeInput(attrs={'class': 'form-control', 'type':'datetime-local'}),
            'fecha_fin': forms.DateTimeInput(attrs={'class': 'form-control', 'type':'datetime-local'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }   

