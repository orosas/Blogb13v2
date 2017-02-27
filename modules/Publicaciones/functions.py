import os
from django.conf import settings

def handle_uploaded_file(f,name):
	root = settings.MEDIA_ROOT+'/Publicaciones/'+name
	with open(root, 'wb+') as destionation:
		for chunk in f.chunks():
			destionation.write(chunk)

	return root

# Nota: Crear funciones que no depende de la aplicación en sí
