from django.shortcuts import render, redirect
from apps.usuario.models import Usuario
from django.template import loader, Context
from django.views.generic import ListView
from .forms import Denuncias


def denunciar(request):

    if request.method == ('POST'):
        form = Denuncias(request.POST)
        if form.is_valid():
            form.save()
            return redirect('denuncias/denuncias.html')
    else:
        form = Denuncias()

    return render(request, 'index.html', {'form' : form })
