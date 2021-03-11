from django import forms
from apps.base_datos.models import Denuncias

class Denuncias(forms.ModelForm):

    class Meta:
        model = Denuncias

        fields = [
            'id_duenio',
            'id_nvo_duenio',
            'descripcion',
        ]

        labels = {
            'id_duenio': user.first_name,
            'id_nvo_duenio': 'Denunciado',
            'descripcion': 'Escriba su denuncia',

        }

        widgets = {
            'id_nvo_duenio': forms.Select(),
            'descripcion': forms.TextInput(),
        }


