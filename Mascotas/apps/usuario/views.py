from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
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

    form = RegistroForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('usuario/Usuario.html')
    else:
        form = RegistroForm()

    return render(request, 'usuario/registro.html', {'form' : form })

def login(request):
    username = request.POST.get("username", "default value")
    password = request.POST.get("password", "default value")
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")


class logout(LogoutView):
    pass

class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = "ModificarUsuario.html"

