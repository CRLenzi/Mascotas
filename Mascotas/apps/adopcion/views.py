from django.http import HttpResponse, HttpResponseRedirect
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
from apps.usuario.models import Usuario


class adoptar(DetailView):
	model = MascotasAdopcion
class adopcionList(ListView):
	model = MascotasAdopcion
	template_name = "adopcion/adopciones.html"


class adopcionCreate(CreateView):
	model = MascotasAdopcion
	template_name = 'adopcion/nueva_adopcion.html'
	form_class = nueva_adopcion
	success_url = reverse_lazy('adopciones')

	def get_context_data(self, **kwargs):
		context = super(adopcionCreate, self).get_context_data(**kwargs)
		context['id_usuario_fk'] = id
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid() :
			adopcion = form.save(commit=False)
			adopcion.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form))



class adopcionUpdate(UpdateView):
	model = MascotasAdopcion
	form_class = nueva_adopcion
	template_name = 'adopcion/modificaradopcion.html'
	success_url = reverse_lazy('adopciones')





