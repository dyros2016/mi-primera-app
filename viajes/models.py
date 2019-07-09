from django.db import models
#from __future__ import incode_literals

class Material(models.Model):
	nombre= models.CharField(max_length=25)
	MEDIDAS = (
        ( 'm3','metros cubicos'),
        ('kg', 'kilogramos'),
        ('lbs','libras')
    )
	medida=models.CharField(max_length=5, choices=MEDIDAS)

	def __str__(self):
		return self.nombre

class Vehiculo (models.Model):

	placa= models.CharField(max_length=8)
	marca= models.CharField(max_length=25)
	modelo=models.CharField(max_length=25)
	def __str__(self):
		return self.placa
class Chofer (models.Model):

	cedula=models.CharField(max_length=10)
	nombre=models.CharField(max_length=25)
	apellido=models.CharField(max_length=25)

	def __str__(self):
		return self.nombre

class Sucursal(models.Model):
	nombre=models.CharField(max_length=25)
	ubicacion = models.CharField(max_length=30, blank=True)
	telefono = models.CharField(max_length=30, blank=True)
	#logo=models.ImageField(upload_to='pic_floder/',default='pic_folder/None/no-img.jpg')

class Proveedor(models.Model):
	nombre=models.CharField(max_length=25)
	propietario=models.CharField(max_length=25)
	direccion=models.CharField(max_length=25)
	def __str__(self):
		return self.nombre



class Orden(models.Model):
	fecha= models.DateTimeField()
	#horae=models.DateField(blank=True,null=True)
	#horas=models.DateField(blank=True,null=True)
	material=models.ForeignKey(Material,on_delete=models.CASCADE)
	proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
	cantidad=models.IntegerField()
	chofer=models.ForeignKey(Chofer,on_delete=models.CASCADE)
	#cedula=models.CharField(max_length=10)
	vehiculo=models.ForeignKey(Vehiculo,on_delete=models.CASCADE)
	#placa=models.CharField(max_length=7)
	entrega=models.CharField(max_length=15)
	recibe=models.CharField(max_length=15)
	#respaldo=models.ImageField(upload_to="recibos")
	def __str__(self):
		return '%s %s %s %s' % (self.id, self.fecha,self.material,self.cantidad)




# Create your models here.
