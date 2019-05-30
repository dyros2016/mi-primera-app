from django.contrib import admin

# Register your models here.
from .models import Material,Vehiculo

admin.site.register(Material)
admin.site.register(Vehiculo)