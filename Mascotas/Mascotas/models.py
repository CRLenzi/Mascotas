# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adopcion(models.Model):
    id_duenio = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_duenio', primary_key=True)
    id_nvo_duenio = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_nvo_duenio', blank=True, null=True)
    id_mascotas = models.ForeignKey('MascotasAdopcion', models.DO_NOTHING, db_column='id_Mascotas')  # Field name made lowercase.
    descripcion = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adopcion'
        unique_together = (('id_duenio', 'id_mascotas'),)


class Denuncias(models.Model):
    id_denuncia = models.AutoField(db_column='id_Denuncia', primary_key=True)  # Field name made lowercase.
    id_duenio = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_duenio')
    id_nvo_duenio = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_nvo_duenio', blank=True, null=True)
    descripcion = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'denuncias'
        unique_together = (('id_denuncia', 'id_duenio'),)


class MascotaTransito(models.Model):
    t_mascotas = models.AutoField(db_column='T_Mascotas', primary_key=True)  # Field name made lowercase.
    id_usuario_fk = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_Usuario_fk')  # Field name made lowercase.
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    edad = models.CharField(max_length=10, blank=True, null=True)
    tiempo = models.CharField(db_column='Tiempo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    vacunas = models.IntegerField()
    castracion = models.IntegerField()
    atencion_especial = models.IntegerField()
    des_at_especial = models.CharField(max_length=200, blank=True, null=True)
    estado = models.IntegerField()
    imagen = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mascota_transito'
        unique_together = (('t_mascotas', 'id_usuario_fk'),)


class MascotasAdopcion(models.Model):
    a_mascotas = models.AutoField(db_column='A_Mascotas', primary_key=True)  # Field name made lowercase.
    id_usuario_fk = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_Usuario_fk')  # Field name made lowercase.
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


class Transito(models.Model):
    id_duenio = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_duenio', primary_key=True)
    id_nvo_duenio = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_nvo_duenio', blank=True, null=True)
    id_mascotas = models.ForeignKey(MascotaTransito, models.DO_NOTHING, db_column='id_Mascotas')  # Field name made lowercase.
    descripcion = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transito'
        unique_together = (('id_duenio', 'id_mascotas'),)


class Usuario(models.Model):
    id_usuario = models.AutoField(db_column='id_Usuario', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Veterinarias(models.Model):
    id_vet = models.AutoField(db_column='id_Vet', primary_key=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=12, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veterinarias'
