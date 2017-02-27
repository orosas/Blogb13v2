from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Publicacion
from django.contrib.auth.models import User
import json
# Create your tests here.

# Test a 
class PublicacionListTest(APITestCase):

	def setUp(self):
		self.user = User.objects.create_superuser(username="userprueba",
						email="user1@gmail.com", password="Blog2016")
		#user = User.objects.get(id=1)
		self.data = {"nombre":"Otra Publicación", 
					"contenido": "Lorem ipsum dolor sit am",
					"tags":"TC",
					"autor":self.user.id
			}
		self.url = reverse('api-list-publicacion')

	def test_list_publicaciones(self):
		
		# self.client viene de APITest
		response = self.client.get(self.url)
		self.assertEqual(response.status_code,status.HTTP_200_OK)

	# Se prueba POST de api-list-publicacion
	def test_create_publicaciones(self):
		response = self.client.post(self.url, self.data,format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		#self.assertEqual(response.data,self.data)


class PublicacionDetailTest(APITestCase):

	def setUp(self):
		self.user = User.objects.create_superuser(username="userprueba",
							email="user1@gmail.com", password="Blog2016")
		self.data = {"nombre":"Otra Publicación", 
					"contenido": "Lorem ipsum dolor sit am",
					"tags":"TC",
					"autor":self.user.id
			}
		self.publicacion = Publicacion(nombre="Otra Publicación",
								contenido="asdfasdfasdfas",
								tags = "TC",
								autor = self.user,
								)
		self.publicacion.save()
		self.url = reverse('api-detail-publicaciones',args=[self.publicacion.id])

	def test_retrieve_publicaciones(self):

		response = self.client.get(self.url)
		#print("########")

		#print(response.content)
		#print("########")		
		self.assertEqual(response.status_code,status.HTTP_200_OK)

	def test_update_publicacion(self):
		self.data = {"nombre":"Otra Publicación",
					"contenido":"asdfasdfasdfas",
					"fecha":"2017-02-21",
					"tags":"TC","autor":3}
		self.data['tags'] = 'PR'
		response = self.client.put(self.url,self.data,format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_delete_publicacion(self):
		response = self.client.delete(self.url)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)




