from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
#from .serializers import UserSerializer,UserSecondSerializer

# PARA LA SEGUNDA class UserDetail
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import generics, filters

# Para clase de filtros
from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework import filters



#Vistas basadas en clases

class UserList(APIView):
    
    def get(self,request):
        #Se pide todo los usuarios
        user = User.objects.all()
        serializer = UserFirstSerializer(user,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        #Se crea el usuario
        # request.data son los datos dentro del body
        serializer = UserSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Métodos para completar el CRUD
class UserDetail(APIView):

    #
    def get(self, request, pk):

        user = get_object_or_404(User,pk=pk)

        if user is not None:
            serializer = UserFirstSerializer(user)
            return Response(serializer.data, status = status.HTTP_200_OK)

    # Para modificar un registro individual de usuario en la base
    def put(self, request,pk):
        user = get_object_or_404(User,pk=pk)

        if user is not None:
            serializer = UserFirstSerializer(instance=user,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User,pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# va a utilizar una url como
# http://127.0.0.1:8000/api/v1/users/publicacionesapi
class PublicacionList(APIView):

    def get(self,request):
        publicaciones = Publicacion.objects.all()

        serializer = PublicacionSecondSerializer(publicaciones,many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

###############################################################
###############################################################
# Genericas
# usa urls: 
# url(r'^publicacionesapi/$', PublicacionList.as_view()),
# url(r'^publicacionesapi/(?P<pk>[0-9]+)/$', PublicacionDetail.as_view()),
# Clase genérica para generar el get y post al igual que el class UserList
# Va a usar:
# http://127.0.0.1:8000/api/v1/users/publicacionesapi/1/
# 

"""
class PublicacionList(generics.ListCreateAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
"""
# Usa from django_filters.rest_framework import DjangoFilterBackend 
# y from rest_framework import generics, filters
class PublicacionList(generics.ListCreateAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    # filtra de manera independiente al input que aparece con search_fields
    filter_fields = ('fecha',)
    search_fields = ('nombre', 'tags',)

    """
    # Filtra pasando el parámetro de la forma:
    #http://127.0.0.1:8000/api/v1/users/publicacionesapi/?publicacion=Primer Post
    def get_queryset(self):

        queryset = Publicacion.objects.all()
        name = self.request.query_params.get('publicacion', None)

        if name is not None:
            queryset = Publicacion.objects.filter(nombre__icontains=name)
        return queryset
    """

# Clase genérica que hace lo mismo que Userdetail get, put y delete (RetrieveUpdateDestroy)
class PublicacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer

