from django.db import models
from Mascotas.Settings import base
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=11, blank=True)
    direccion = models.CharField(max_length=20, blank=True)

 
