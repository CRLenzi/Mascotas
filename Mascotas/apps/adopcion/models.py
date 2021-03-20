from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.usuario.models import Usuario


# Create your models here.
class MascotasAdopcion(models.Model):
    a_nombre = models.CharField(max_length=11, blank=True)
    id_usuario_fk = models.ForeignKey(Usuario,on_delete=models.CASCADE)  
    sexo = models.CharField(max_length=10, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    imagen = models.TextField(blank=True, null=True)
    edad = models.CharField(max_length=10, blank=True, null=True)
    estado = models.IntegerField()

    class Meta:
        db_table = 'mascotas_adopcion'