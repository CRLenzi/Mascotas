
from django.db import models
from Mascotas.Settings import base
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    id = models.AutoField(db_column='id', primary_key=True)
    telefono = models.CharField(max_length=11, blank=True)
    direccion = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return '{} {}' .format(self.user.first_name, self.user.last_name)
