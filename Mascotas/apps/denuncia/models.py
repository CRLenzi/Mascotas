from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.usuario.models import Usuario


class Denuncias(models.Model):
    denunciante = models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name='denunciante')
    denunciado = models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name='denunciado')
    descripcion = models.CharField(max_length=250)

    class Meta:
        db_table = 'denuncias'

