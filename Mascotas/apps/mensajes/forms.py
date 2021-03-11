from django import forms
from apps.usuario.models import Usuario
from .models import Mensajes


class mensaje(forms.ModelForm):

	class Meta:
		model = Mensajes
		fields = [
			'emisor',
			'receptor',
			'id_mascotas',
			'mensaje',
		]

		labels = {
			'emisor' :'emisor',
			'receptor':'receptor',
			'id_mascotas':'id_mascota',
			'mensaje':'mensaje',
		}
		widgets = {
			'mensaje': forms.TextInput(),
		}