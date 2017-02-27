from django.db import models
# Importamos modelo de usuarios
from django.contrib.auth.models import User
#import psycopg2

TAGS = (
	('TC', 'Tecnología'),
	('CT', 'Científico'),
	('PR', 'Programación'),
	)


"""
Nota Omar: Si se deja el manager, desde el Admin no se ven los Post


class PepePublicacionesManager(models.Manager):
	def get_queryset(self):
		return super(PepePublicacionesManager,self).get_queryset().filter(autor__username="Pepe")
"""



class Publicacion(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=50)
	contenido = models.TextField()
	fecha = models.DateField(auto_now_add=True) # Timestamp
	autor = models.ForeignKey(User,on_delete=models.CASCADE, related_name='publicaciones') # Pasar el modelo con el cual se va a relacionar
	tags = models.CharField(choices=TAGS, max_length=50)
	imagen = models.ImageField(upload_to='Publicaciones/',null=True, blank=True)


	#pepe_publish = PepePublicacionesManager() Se comenta manager porque en admin no se ven los post registrados

	def __str__(self):
		return "%s %s" % ("Publicacion: ", self.nombre)

