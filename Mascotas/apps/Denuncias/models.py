from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.usuario.models import Usuario
from Mascotas.Settings import base

class Denuncias(models.Model):
    id_denuncia = models.AutoField(db_column='id_Denuncia', primary_key=True)  # Field name made lowercase.
    denunciante = models.ForeignKey(base.AUTH_USER_MODEL, db_column='denunciante',related_name='denunciante', on_delete=models.CASCADE)
    denunciado = models.ForeignKey(base.AUTH_USER_MODEL, db_column='denunciado', blank=True, null=True, related_name='denunciado', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'denuncias'
        unique_together = (('id_denuncia', 'denunciante'),)