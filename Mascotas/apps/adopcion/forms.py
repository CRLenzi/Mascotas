from django import forms
from .models import MascotasAdopcion

class nueva_adopcion(forms.ModelForm):

    class Meta:
        model = MascotasAdopcion

        fields = [
             'a_nombre',
             'sexo',
             'descripcion',
             'imagen',
             'edad',
             'estado',
        ]

        labels = {
            'a_nombre' : "Nombre",
            'sexo' : "Sexo",
            'descripcion': "Descripcion de la mascota",
            'imagen' : "Imagen de la mascota",
            'edad' : "Edad",
            'estado': False,

        }

        widgets = {
             'a_nombre' : forms.TextInput(),
             'sexo': forms.TextInput(),
             'descripcion': forms.TextInput(),
             'imagen': forms.FileInput(),
             'edad': forms.TextInput(),
        }


