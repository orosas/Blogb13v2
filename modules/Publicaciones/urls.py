from django.conf.urls import url
from .views import Index, Add

# para usar viewsets
#from rest_framework.routers import DefaultRouter
#from .api_viewset import PublicacionViewset

#router = DefaultRouter()
#router.register(r'^viewsets/$', PublicacionViewset)
#urls = router.urls
"""
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', Index, name='index-publicacion'),
    url(r'^add/$', Add, name='add-publicaciones'),
] + urls
"""
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', Index, name='index-publicacion'),
    url(r'^add/$', Add, name='add-publicaciones'),
]