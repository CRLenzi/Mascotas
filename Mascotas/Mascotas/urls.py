"""Mascotas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Mascotas.view import inicio
from apps.usuario.views import registro, login, logout
from apps.adopcion.views import adopcion, adoptar, nva_adopcion, adopcionUpdate, adopcionCreate, adopcionList
from apps.mensaje.views import Chats, Mensajes
from apps.denuncia.views import denunciar
"""aca van las vistas o views"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name = 'inicio'),

    path('registro/', registro, name= 'registro'),
    path('login/', login, name='login'),
    path('logout/', logout.as_view(), name='logout'),
    
    path('adoptar/<int:mascota_id>', adoptar.as_view(), name= 'adoptar'),
    path('adopciones/', adopcionList.as_view(), name= 'adopcion'),
    path ('nueva/', adopcionCreate.as_view(), name= 'nuevaadopcion'),
    
    path('denuncias/', denunciar, name= 'denuncias'),

    path('chat/',Chats, name= 'chat'),
    path('Mensajes/<int:emisor>/<int:receptor>/<int:mascota_id>', Mensajes, name= 'mensaje'),

]
