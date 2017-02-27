from django.shortcuts import render, redirect
from .models import TAGS, Publicacion
from .functions import handle_uploaded_file

# Create your views here.
def Index(request):
	public = [
		{
			"Nombre":"Mi primer Proyecto en Django",
			"Autor":"Omar Rosas",
			"Fecha":"7-02-2017",
			"Ratings":1
		},
		{
			"Nombre":"Segundo Nombre",
			"Autor":"Autor 2",
			"Fecha":"08-02-2017",
			"Ratings":2
		},
		{
			"Nombre":"Nombre 03",
			"Autor":"Autor 03",
			"Fecha":"9-02-2017",
			"Ratings":3
		},
	]	

	return render(request, 'Publicaciones/index.html', {"publicaciones":public})

def Add(request):
# En lugar de hardcodear TAGS se importa del model	
	if request.method == 'POST':
		if request.user.is_authenticated():
			types = {'image/jpg':'.jpg','image/png':'.png','image/gif':'.gif'}
			image_name = request.FILES['imagen'].name+types[request.FILES['imagen'].content_type]

			publicacion = Publicacion()

			publicacion.nombre = request.POST['nombre']
			publicacion.contenido = request.POST['contenido']
			publicacion.tags = request.POST['tag']
			publicacion.autor = request.user
			publicacion.imagen = handle_uploaded_file(request.FILES['imagen'],image_name)

			publicacion.save()

			return redirect('Publicaciones:index-publicacion')
	else:
		dict_tags = dict((x,y) for x,y in TAGS)
		return render(request,'Publicaciones/add.html', {"tags":dict_tags})
		print(dict_tags)