from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.template import loader, Context
from django.views.generic import ListView, UpdateView,CreateView
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Usuario
from .forms import RegistroForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy




class registro(CreateView):
    model = Usuario
    template_name = "usuario/registro.html"
    form_class = RegistroForm
    success_url = reverse_lazy ('inicio')



class logout(LogoutView):
    pass

class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = "ModificarUsuario.html"

