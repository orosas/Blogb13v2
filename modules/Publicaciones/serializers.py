from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Publicacion
#from modules.Publicaciones.serializers import PublicacionSerializer

# para tablas que están relacionadas
# es la tercera clase del ejemplo, pero se mueve al principio
class PublicacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publicacion
        fields = ('nombre', 'contenido', 'fecha', 'tags', 'autor')

class UserFirstSerializer(serializers.ModelSerializer):

    # Siguiente línea indica las publicaciones del usuario
    publicaciones = PublicacionSerializer(read_only=True,many=True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'is_active',
            'publicaciones'
            )
        #todos los campos field = ('__ALL__')
class UserSecondSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('is_active',)

# Class para llamar "datos" de tablas "cruzadas"
# 
class PublicacionSecondSerializer(serializers.ModelSerializer,serializers.Serializer):

    writer_username = serializers.CharField(source='autor.username')
    #writer_lastname = serializers.CharField(source='autor.apaterno')
    class Meta:
        model = Publicacion
        fields = ('nombre', 'contenido', 'fecha', 'tags', 'writer_username',)
