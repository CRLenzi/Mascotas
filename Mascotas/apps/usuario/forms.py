from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):

	class Meta:
		model = Usuario
		fields = [
			'first_name',
			'last_name',
			'username',
			'is_staff',
			'telefono',
			'direccion',
		]

		labels = {
			'first_name': 'Nombre',
			'last_name': 'Apellidos',
			'username': 'email',
			'is_staff': False,
			'telefono': 'telefono',
			'direccion': 'direccion',
		}

		widgets = {
			'first_name': forms.TextInput(),
			'last_name': forms.TextInput(),
			'username': forms.TextInput(),
			'telefono': forms.TextInput(),
			'direccion': forms.TextInput(),
		}
