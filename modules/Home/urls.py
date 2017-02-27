from django.conf.urls import url
from .views import Index, Contacto, Otros, Sumar, Saludo, Mayorque, Signup, Login, Logout # Se deben importar las views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', Index, name='index'),
    url(r'^contacto$', Contacto, name='contacto'),
    url(r'^otros/(?P<num>[0-9]+)/$', Otros, name='otros'),
    url(r'^sumar/(?P<num1>[0-9]+)/(?P<num2>[0-9]+)/$', Sumar, name='sumar'),
    url(r'^saludo/(?P<nombre>[\w]+)/$', Saludo, name='saludo'),
    url(r'^mayorque/(?P<num1>[0-9]+)/(?P<num2>[0-9]+)/$', Mayorque, name='mayorque'),
    url(r'^signup/$', Signup, name='Signup'),
    url(r'^login/$', Login, name='Login'),
    url(r'^logout/$', Logout, name='Logout'),
]
