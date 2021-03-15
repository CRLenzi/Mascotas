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
             'vacunas',
             'castracion',
             'atencion_especial',
             'des_at_especial',  
        ]

        labels = {
            'a_nombre' : "Nombre",
            'sexo' : "Sexo",
            'descripcion': "Descripcion de la mascota",
            'imagen' : "Imagen de la mascota",
            'edad' : "Edad",
            'vacunas' : "¿Tiene todas sus vacunas al dia?",
            'castracion' : "¿Esta castrado?",
            'atencion_especial' : "¿Requiere atencion especial?",
            'des_at_especial' : "Si res´pondio antes que si por favor especifique cual",

        }

        widgets = {
             'a_nombre' : forms.TextInput(),
             'sexo': forms.TextInput(),
             'descripcion': forms.TextInput(),
             'imagen': forms.FileInput(),
             'edad': forms.TextInput(),
             'vacunas':forms.CheckboxInput(),
             'castracion': forms.CheckboxInput(),
             'atencion_especial': forms.CheckboxInput(),
             'des_at_especial': forms.TextInput(),
        }


