from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.usuario.models import Usuario

class Denuncias(models.Model):
    id_denuncia = models.AutoField(db_column='id_Denuncia', primary_key=True)  # Field name made lowercase.
    denunciante = models.ForeignKey(User, db_column='id_duenio',related_name='denunciante', on_delete=models.CASCADE)
    denunciado = models.ForeignKey(User, db_column='id_nvo_duenio', blank=True, null=True, related_name='denunciado', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'denuncias'
        unique_together = (('id_denuncia', 'id_duenio'),)