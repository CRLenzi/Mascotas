from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.template import loader, Context
from django.views.generic import ListView, CreateView
from .forms import mensaje
from apps.usuario.models import Usuario
from django.urls import reverse_lazy

# Create your views here.

def Chats(request):
    chat = Mensajes.objects.grup_by(emisor,receptor).filter(emisor = request.user.id).order_by(creado).values(emisor, receptor, mascota_id)

    Context ={
        chat,
    }

    return render(request, 'chat', Context)
    

def Mensajes(request, emisor, receptor, mascota_id ):
    u1 = Usuario.objects.get(id=emisor)
    u2 = Usuario.objects.get(id=receptor)
    m = Mensajes.objects.create(emisior=u1, receptor=u2, id_mascotas= mascota_id)

    return redirect('Mensajes')
