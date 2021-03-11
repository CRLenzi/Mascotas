from django.shortcuts import render, redirect
from apps.base_datos.models import Usuarios, Denuncias
from django.template import loader, Context
from django.views.generic import ListView
from .form import Denuncias


def denunciar(request):

    if request.method == ('POST'):
        form = Denuncias(request.POST)
        if form.is_valid():
            form.save()
            return redirect('denuncias/denuncias.html')
    else:
        form = Denuncias()

    return render(request, 'index.html', {'form' : form })
