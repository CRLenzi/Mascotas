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

def saludo(request):
	
	return render(request, "index.html")

def adopcion(request):

    t = MascotasAdopcion.objects.exclude(estado=0)
    context = {"Mascota": t}
    return render (request, "adopciones.html", context)

def nva_adopcion(request, mascota):

    t = loader.get_template('adoptar.html')
    c = Context(mascota)

    return t.render(c)

def denuncias(request):
	
	return render(request, "denuncias.html")

def veterinaria(request):
	
	return render(request, "veterinarias.html")

def transito(request):
	
	return render(request, "transito.html")

def registro(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
	
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

	

    # Si llegamos al final renderizamos el formulario
    return render(request, "registro.html", {'form': form})

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})

def adoptar(request):
    # Si estamos identificados permitimos la adopcion
    if request.user.is_authenticated:
        return render(request, "adoptar.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')