from django.db import models
from apps.adopcion.models import MascotasAdopcion
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.usuario.models import Usuario



class Mensajes(models.Model):
    receptor = models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name='receptor')
    emisor = models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name='emisor')
    id_mascotas = models.ForeignKey(MascotasAdopcion,on_delete=models.CASCADE, null = False)  # Field name made lowercase.
    creado = models.DateTimeField(auto_now_add=True,verbose_name=u'creado',help_text=u'Fecha de creación')
    mensaje = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'Mensajes'

