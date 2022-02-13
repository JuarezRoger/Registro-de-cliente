from django.db import models

class Sexo(models.Model):
	sexo = models.CharField(max_length=10)

	def __str__(self):
		return self.sexo

class Cliente(models.Model):
	identidad = models.CharField(max_length=16)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	direccion = models.TextField()
	sexo = models.ForeignKey(Sexo, on_delete=models.PROTECT)

	def __str__(self):
		return self.nombre
