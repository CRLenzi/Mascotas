from django import forms
from .models import MascotasAdopcion
from apps.usuario.models import Usuario


class nueva_adopcion(forms.ModelForm):

	class Meta:
		model = MascotasAdopcion

		fields = [
			 'a_nombre',
			 'id_usuario_fk',
			 'sexo',
			 'descripcion',
			 'imagen',
			 'edad',
		]

		labels = {
			'a_nombre' : "Nombre",
			'sexo' : "Sexo",
			'descripcion': "Descripcion de la mascota",
			'imagen' : "Imagen de la mascota",
			'edad' : "Edad",
			'estado' : False,

		}

		widgets = {
			 'a_nombre' : forms.TextInput(),
			 'sexo': forms.TextInput(),
			 'descripcion': forms.TextInput(),
			 'imagen': forms.FileInput(),
			 'edad': forms.TextInput(),
		}


