from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.usuario.models import Usuario


class MascotaTransito(models.Model):
    t_mascotas = models.AutoField(db_column='T_Mascotas', primary_key=True)  # Field name made lowercase.
    t_nombre = models.CharField(max_length=11, blank=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    id_usuario_fk = models.ForeignKey(User, db_column='id_Usuario_fk',on_delete=models.CASCADE)  # Field name made lowercase.
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    edad = models.CharField(max_length=10, blank=True, null=True)
    tiempo = models.CharField(db_column='Tiempo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    vacunas = models.IntegerField(blank=True, null=True)
    castracion = models.IntegerField(blank=True, null=True)
    atencion_especial = models.IntegerField(blank=True, null=True)
    des_at_especial = models.CharField(max_length=200, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    imagen = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mascota_transito'
        unique_together = (('t_mascotas', 'id_usuario_fk'),)
