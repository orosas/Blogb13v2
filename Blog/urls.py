"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# para cargar media y static
from django.conf import settings
from django.conf.urls.static import static
# Par django rest framework
from .api_urls import urlpatterns as api_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('modules.Home.urls', namespace='Home', app_name='Home'), name="Home"),
    url(r'^publicaciones/', include('modules.Publicaciones.urls', namespace='Publicaciones', app_name='Publicaciones')),
    url(r'^nasa/', include('modules.Nasa.urls', namespace='Nasa', app_name='Nasa'), name="Nasa"),
    #urls api
    url(r'^api/v1/', include(api_urls)),
]
