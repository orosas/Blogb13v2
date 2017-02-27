from django.conf.urls import url
from .views import Consulta

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', Consulta, name='consulta-api'),
]