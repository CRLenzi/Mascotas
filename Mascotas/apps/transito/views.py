from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from .models import  MascotaTransito
from apps.usuario.models import Usuario
from django.template import loader, Context
from django.views.generic import ListView, UpdateView, CreateView
from .forms import nuevo_transito
from django.urls import reverse_lazy


def transito(request):

	t = MascotaTransito.objects.filter(estado=False)
    
	ctx = {
        "Transito": t
	}

	return render(request, "transito/transito.html", ctx)


class transitoList(ListView):
    model = MascotaTransito
    template_name = "transito/transito.html"

class transitoCreate(CreateView):
    model = MascotaTransito
    form_class = nuevo_transito
    template_name = 'transito/nuevo_transito.html'
    success_url = reverse_lazy('nuevotransito')


class TransitoUpdate(UpdateView):
    model = MascotaTransito
    template_name = "transito/modificartransito.html"
