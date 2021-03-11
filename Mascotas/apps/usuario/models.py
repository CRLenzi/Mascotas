
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=11, blank=True)
    direccion = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return '{} {}' .format(self.user.first_name, self.user.last_name)