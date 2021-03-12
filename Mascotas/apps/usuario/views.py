from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.template import loader, Context
from django.views.generic import ListView, UpdateView
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Usuario
from .forms import RegistroForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


def registro(request):

    if request.method == ('POST'):
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario/Usuario.html')
    else:
        form = RegistroForm()

    return render(request, 'usuario/registro.html', {'form' : form })


class login(LoginView):
    model = Usuario
    template_name = 'Usuario/login.html'
    success_url = reverse_lazy('inicio')

class logout(LogoutView):
    pass

class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = "ModificarUsuario.html"




