from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):

	class Meta:
		model = Usuario
		fields = [
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
			'is_staff',
			'telefono',
			'direccion',
		]

		labels = {
			'first_name': 'Nombre',
			'last_name': 'Apellidos',
			'password1': 'Ingrese su contraseña',
			'password2': 'Ingrese nuevamente su contraseña',
			'email': 'Correo electronico',
			'is_staff': False,
			'telefono': 'telefono',
			'direccion': 'direccion',
		}

		widgets = {
			'first_name': forms.TextInput(),
			'last_name': forms.TextInput(),
			'email': forms.TextInput(),
			'password1' :forms.PasswordInput(),
			'password2': forms.PasswordInput(),
			'telefono': forms.TextInput(),
			'direccion': forms.TextInput(),
		}
