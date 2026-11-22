
from django import forms
from .models import Aprendiz, Programa, Instructores, Competencias, Local


class AprendizForm(forms.ModelForm):

    class Meta:
        model = Aprendiz

        fields = ['Programa','nombre','apellido','documento','tipo_documento', 'correo', 'telefono', 'ficha']

        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el nombre'}),
                    'apellido': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el apellido'}),
                    'documento': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Ingrese el documento'}),
                    'tipo_documento': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ejemplo: C.C.'}),
                    'correo': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Ingrese el correo electrónico'}),
                    'telefono': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Ingrese el teléfono'}),
                    'ficha': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Ingrese el número de ficha'}),
                    'Programa': forms.Select(attrs={'class': 'form-control'})
        }
class ProgramaForm(forms.ModelForm):

    class Meta:
        model = Programa
        fields = ['nombre', 'ficha','jornada','lugar','duracion','modalidad', 'nivel_profesional', 'descripcion']


class InstructoresForm(forms.ModelForm):

    class Meta:
        model = Instructores
        fields = ['nombre', 'apellido','documento','telefono','especialidad', 'ficha_asignada', 'correo']


class CompetenciasForm(forms.ModelForm):

    class Meta:
        model = Competencias
        fields = ['nombre', 'ficha','instructores']
        
    
class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = [
            'nombre',
            'direccion',
            'lat',
            'lng',
        ]
        widgets = {
            'lat': forms.NumberInput(attrs={'step': 'any'}),
            'lng': forms.NumberInput(attrs={'step': 'any'}),
        }
    
       