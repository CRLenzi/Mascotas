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


"""aca iran todas las vistas"""

def inicio(request):
	
	return render(request, "inicio.html")

def denuncias(request):
	
	return render(request, "denuncias.html")

def veterinaria(request):
	
	return render(request, "veterinarias.html")



