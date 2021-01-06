from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
import datetime



# formulario contacto para vista contacto
class Contacto(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()

# formulario Palabra para vista contador de palabras
class Palabra(forms.Form):
    palabra = forms.CharField()

# TAREAS PENDIENTES faltan crear otros dos formularios para las vistas
# agregar imagen y agregar contenido






# CODIGO DEL PROFE 
class PrimerFormulario(forms.Form):
    marca = forms.CharField(
                widget = forms.TextInput(
                                attrs = {'style': 'border-color: blue;'}),
                validators=[validators.MinLengthValidator(
                        4, 
                        "Marca debe tener 4 caracteres mínimo!")])
    modelo = forms.CharField(validators=[validators.MinLengthValidator(2, 
                            "El modelo no puede ser de menos de 2 letras")
                        	  ])
    cuerdas = forms.IntegerField(
                validators=[validators.MaxValueValidator(10, "Número entre 6 y 10"),
                        validators.MinValueValidator(6,"Número entre 6 y 10"),])
    fecha_compra = forms.DateField(
                validators=[validar_fecha]
    )





    
