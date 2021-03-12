from django import forms
from apps.usuario.models import Usuario
from .models import Denuncias

class Denuncias(forms.ModelForm):

    class Meta:
        model = Denuncias

        fields = [
            'denunciante',
            'denunciado',
            'descripcion',
        ]

        labels = {
            'denunciante': Usuario.id,
            'denunciado': 'Denunciado',
            'descripcion': 'Escriba su denuncia',

        }

        widgets = {
            'denunciado': forms.Select(),
            'descripcion': forms.TextInput(),
        }


