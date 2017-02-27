from django.shortcuts import render, get_object_or_404, redirect # Redirect se usa en view login
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms  import LoginForm # para view login
from django.contrib.auth import authenticate, login, logout # para crear una sesión dentro del sistema view login


# Create your view here.

def Index(request):
	user = request.user
	return render(request,'Home/index.html', {"user":user})

def Contacto(request):
	return HttpResponse('Pagina de contactos')

def Otros(request,num):
	return HttpResponse('Pagina de otros con el numero:  <b> '+num+'</b>')

def Sumar(request,num1, num2):

	lasuma = int(num1) + int(num2)
	return HttpResponse('La suma de: '+ str(num1) +' y '+ str(num2) +' es ='+ str(lasuma) )

def Saludo(request,nombre):

	return HttpResponse('Hola '+nombre )

def Mayorque(request, num1, num2):
	if int(num1) > int(num2):
		return HttpResponse('Parametro 1: '+num1+' es mayor que Parametro 2: '+num2)
	else:
		return HttpResponse('Parametro 2: '+num2+' es mayor que Parametro 1: '+num1)


"""
Nota Omar: Primera versión 

def Signup(request):

	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']

		user = User.objects.create_user(
				first_name=first_name,
				last_name=last_name,
				username=username,
				password=password,
				email=email
			)

		user.save()
		return HttpResponse('<b>Usuario Registrado</b>')
	else:
		return render(request,'Home/signup.html')
"""

def Signup(request):

	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		print("Dentro de if ....")

		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			user = None
		
		if user is None:
			user = User.objects.create_user(
				first_name=first_name,
				last_name=last_name,
				username=username,
				password=password,
				email=email
			)
			user.save()
			return HttpResponse('<b>Usuario Registrado</b>')
		else:
			return HttpResponse('<b>El Usuario que ingresaste ya existe</b>')
	else:
		return render(request,'Home/signup.html')



"""

OMAR: Ejemplo que no funciona

def Login(request):

	if request.method == 'POST':
		loginform = LoginForm(request.POST) # pasando diccionario de post al form

		if loginform.is_valid():

			user = get_object_or_404(User, username=loginform.cleaned_data['username'])

			if user is not None:
				login(request,user)

				return redirect('Home:index')
		else:
			return HttpResponse('<b>Data no valida')
	else:
		loginform = LoginForm()
		return render(request, 'Home/login.html',{"form":loginform})

"""

def Login(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])

		if user is not None:
			login(request,user)
			return redirect('Home:index')
		else:
			return HttpResponse("Error en usuario o contraseña")
	else:
		return render(request, 'Home/login.html')

def Logout(request):
	logout(request)
	return redirect('Home:index')


