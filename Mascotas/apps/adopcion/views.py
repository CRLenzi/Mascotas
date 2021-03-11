from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from .models import MascotasAdopcion
from django.template import loader, Context
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from .form import nueva_adopcion
from django.urls import reverse_lazy


def adopcion(request):

	t = MascotasAdopcion.objects.filter(estado__icontains=0)
	#Mysql por defecto no utiliza bool sino tiniint, por lo que 0 = falso y 1 = verdadero
	context = { 
		"Mascota": t
		}
	return render(request, "adopcion/adopciones.html", context)

def nva_adopcion(request):

	if request.user.is_authenticated:
		if request.method == ('POST'):
			form = nueva_adopcion(request.POST)
			if form.is_valid():
				form.save()
				return redirect('adopcion/adopciones.html')
		else:
			form = nueva_adopcion()

		return render(request, 'adopcion/nueva_adopcion.html', {'form' : form })
	
	return redirect('/login')

class adoptar (DetailView):

	model = MascotasAdopcion
class adopcionList(ListView):
	model = MascotasAdopcion
	template_name = "adopcion/adopciones.html"

class adopcionCreate(CreateView):
	model = MascotasAdopcion
	form_class = nueva_adopcion
	template_name = 'adopcion/nueva_adopcion.html'
	success_url = reverse_lazy('adopcion')


class adopcionUpdate(UpdateView):
	model = MascotasAdopcion
	form_class = nueva_adopcion
	template_name = 'adopcion/modificaradopcion.html'
	success_url = reverse_lazy('adopcion')



def get_data(request):
	 if request.method == 'POST':
		 nombre = request.POST.get('')
		 edad = request.POST.get('')
		 descripcion = request.POST.get('')
		 vacunas = request.POST.get('')
		 castracion= request.POST.get('')
		 atencion_especial = request.POST.get('')
		 des_atencion_especial = request.POST.get('')
	 return  data_1, data_2

