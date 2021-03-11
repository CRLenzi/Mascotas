# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.usuario.models import Usuario


class Mensajes(models.Model):
    receptor = models.ForeignKey(User, db_column='id_duenio', primary_key=True,related_name='solicitante',on_delete=models.CASCADE)
    emisor = models.ForeignKey(User, db_column='id_nvo_duenio', blank=True, null=True,on_delete=models.CASCADE)
    id_mascotas = models.ForeignKey('MascotasAdopcion', db_column='id_Mascotas',on_delete=models.CASCADE)  # Field name made lowercase.
    creado = models.DateTimeField(auto_now_add=True,verbose_name=u'creado',help_text=u'Fecha de creación')
    mensaje = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transito'
        unique_together = (('id_duenio', 'id_mascotas'),)

class Veterinarias(models.Model):
    id_vet = models.AutoField(db_column='id_Vet', primary_key=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=12, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veterinarias'
