from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.usuario.models import Usuario

# Create your models here.
class MascotasAdopcion(models.Model):
    a_mascotas = models.AutoField(db_column='A_Mascotas', primary_key=True)  # Field name made lowercase.
    a_nombre = models.CharField(max_length=11, blank=True)
    id_usuario_fk = models.ForeignKey(User, db_column='id_Usuario_fk',on_delete=models.CASCADE)  # Field name made lowercase.
    sexo = models.CharField(max_length=10, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    imagen = models.TextField(blank=True, null=True)
    edad = models.CharField(max_length=10, blank=True, null=True)
    vacunas = models.IntegerField()
    castracion = models.IntegerField()
    atencion_especial = models.IntegerField()
    des_at_especial = models.CharField(max_length=200, blank=True, null=True)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mascotas_adopcion'
        unique_together = (('a_mascotas', 'id_usuario_fk'),)
