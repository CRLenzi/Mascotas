from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from apps.base_datos.models import MascotasAdopcion, MascotaTransito, Adopcion
from django.template import loader, Context
from django.views.generic import ListView


def transito(request):

	t = MascotaTransito.objects.filter(estado=False)
    
	ctx = {
        "Transito": t
	}

	return render(request, "adopcion/transito.html", ctx)