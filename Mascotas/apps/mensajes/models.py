# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from apps.adopcion.models import MascotasAdopcion
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.usuario.models import Usuario
from Mascotas.Settings import base


class Mensajes(models.Model):
    receptor = models.ForeignKey(base.AUTH_USER_MODEL, db_column='receptor', primary_key=True,related_name='solicitante',on_delete=models.CASCADE)
    emisor = models.ForeignKey(base.AUTH_USER_MODEL, db_column='emisor', blank=True, null=True,on_delete=models.CASCADE)
    id_mascotas = models.ForeignKey(MascotasAdopcion, db_column='id_Mascotas',on_delete=models.CASCADE)  # Field name made lowercase.
    creado = models.DateTimeField(auto_now_add=True,verbose_name=u'creado',help_text=u'Fecha de creación')
    mensaje = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mensajes'
        unique_together = (('receptor', 'id_mascotas'),)

