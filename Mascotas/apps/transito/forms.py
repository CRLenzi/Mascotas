from django import forms
from .models import MascotaTransito

class nuevo_transito(forms.ModelForm):

    class Meta:
        model = MascotaTransito

        fields = [
             't_nombre',
             'sexo',
             'descripcion',
             'imagen',
             'edad',
             'tiempo',
             'vacunas',
             'castracion',
             'atencion_especial',
             'des_at_especial',  
        ]

        labels = {
            't_nombre' : "Nombre",
            'sexo' : "Sexo",
            'descripcion': "Descripcion de la mascota",
            'imagen' : "Imagen de la mascota",
            'tiempo' : "¿Por cuanto tiempo requiere transito",
            'edad' : "Edad",
            'vacunas' : "¿Tiene todas sus vacunas al dia?",
            'castracion' : "¿Esta castrado?",
            'atencion_especial' : "¿Requiere atencion especial?",
            'des_at_especial' : "Si res´pondio antes que si por favor especifique cual",

        }

        widgets = {
            't_nombre' : forms.TextInput(),
            'sexo': forms.TextInput(),
            'descripcion': forms.TextInput(),
            'tiempo':forms.TextInput(),
            'edad': forms.TextInput(),
            'vacunas':forms.CheckboxInput(),
            'castracion': forms.CheckboxInput(),
            'atencion_especial': forms.CheckboxInput(),
            'des_at_especial': forms.TextInput(),
            'imagen': forms.FileInput(),
        }


