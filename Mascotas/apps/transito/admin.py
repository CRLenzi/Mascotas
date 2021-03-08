from django.contrib import admin
from apps.base_datos.models import Usuario, MascotaTransito, MascotasAdopcion, Adopcion, Denuncias, Transito, Veterinarias

# Register your models here.
admin.site.register(Usuario)
admin.site.register(MascotasAdopcion)
admin.site.register(MascotaTransito)
admin.site.register(Adopcion)
admin.site.register(Denuncias)
admin.site.register(Transito)
admin.site.register(Veterinarias)

