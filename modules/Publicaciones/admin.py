from django.contrib import admin
from .models import Publicacion

# Register your models here.
class PublicacionAdmin(admin.ModelAdmin):
	pass

admin.site.register(Publicacion, PublicacionAdmin)
