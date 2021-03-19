from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from .models import MascotasAdopcion
from django.template import loader, Context
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from .forms import nueva_adopcion
from django.urls import reverse_lazy


class adoptar(DetailView):

	model = MascotasAdopcion
class adopcionList(ListView):
	model = MascotasAdopcion
	template_name = "adopcion/adopciones.html"

class adopcionCreate(CreateView):
	model = MascotasAdopcion
	form_class = nueva_adopcion
	template_name = 'adopcion/nueva_adopcion.html'
	success_url = reverse_lazy('adopciones')


class adopcionUpdate(UpdateView):
	model = MascotasAdopcion
	form_class = nueva_adopcion
	template_name = 'adopcion/modificaradopcion.html'
	success_url = reverse_lazy('adopciones')





