from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Material(models.Model):
	nombre= models.CharField(max_length=25)
	medida=models.CharField(max_length=5)

class Vehiculo (models.Model):

	placa= models.CharField(max_length=7)
	marca= models.CharField(max_length=25)
	modelo=models.CharField(max_length=25)

class Chofer (models.Model):

	cedula=models.CharField(max_length=10)
	nombre=models.CharField(max_length=25)
	apellido=models.CharField(max_length=25)

class Sucursal(models.Model):
	nombre=models.CharField(max_length=25)
	ubicacion = models.CharField(max_length=30, blank=True)
	telefono = models.CharField(max_length=30, blank=True)
	#logo=models.ImageField(upload_to='pic_floder/',default='pic_folder/None/no-img.jpg')

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
 
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)


class Orden(models.Model):
	fecha= models.DateField()
	hora=models.DateField()
	material=models.ForeignKey(Material,on_delete=models.CASCADE)
	medida=models.CharField(max_length=5)
	cantidad=models.IntegerField()
	chofer=models.ForeignKey(Chofer,on_delete=models.CASCADE)
	#cedula=models.CharField(max_length=10)
	vehiculo=models.ForeignKey(Vehiculo,on_delete=models.CASCADE)
	#placa=models.CharField(max_length=7)
	entrega=models.CharField(max_length=15)
	recibe=models.CharField(max_length=15)
# Create your models here.
