from django.contrib import admin

# Register your models here.
from .models import Material, Vehiculo,Chofer,Proveedor,Orden

admin.site.register(Material)
admin.site.register(Vehiculo)
admin.site.register(Chofer)
admin.site.register(Proveedor)
admin.site.register(Orden)
#admin.site.register(Perfil)
