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



def adoptar(request):
    # Si estamos identificados permitimos la adopcion
    if request.user.is_authenticated:
        return render(request, "adopcion/adoptar.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

def adopcion(request):

    t = MascotasAdopcion.objects.filter(estado=False)
    context = {
        "Mascota": t
        }
    return render(request, "adopcion/adopciones.html", context)

def nva_adopcion(request, mascota):

    t = loader.get_template('adopcion/adoptar.html')
    c = Context(mascota)

    return t.render(c)