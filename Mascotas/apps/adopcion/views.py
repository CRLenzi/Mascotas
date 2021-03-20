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
from apps.usuario.models import Usuario


class adoptar(DetailView):
	model = MascotasAdopcion
class adopcionList(ListView):
	model = MascotasAdopcion
	template_name = "adopcion/adopciones.html"

def adopcionCreate (request, id):

	usuario = Usuario.objects.get(id=id)
	if request.method == ('GET'):
		form = nueva_adopcion(request.POST)
		form.id_usuario_fk = usuario
		form.estado = False
		if form.is_valid():
			form.save()
			return redirect('nuevaadopcion')
	else:
		form = nueva_adopcion()
		return render(request, 'adopcion/nueva_adopcion.html', {'form' : form })

class adopcionCreate(CreateView):
	model = MascotasAdopcion
	template_name = 'adopcion/nueva_adopcion.html'
	form_class = nueva_adopcion
	second_form_class = Usuario
	success_url = reverse_lazy('adopciones')

	def get_context_data(self, **kwargs):
		context = super(adopcionCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			adopcion = form.save(commit=False)
			adopcion.usuario = form2.save()
			adopcion.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))



class adopcionUpdate(UpdateView):
	model = MascotasAdopcion
	form_class = nueva_adopcion
	template_name = 'adopcion/modificaradopcion.html'
	success_url = reverse_lazy('adopciones')





