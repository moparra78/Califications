from django.urls import path
from django.conf.urls import url, include #11oct
from django.contrib.auth.models import User #11oct
from rest_framework import routers, serializers, viewsets #11oct

from . import views
from registro.views import FacultadViewSet #11oct

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter() #11oct
router.register(r'facultad', FacultadViewSet) #11oct

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('registro/', include('registro.urls')),
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)), #11oct
    url(r'^api-auth/', include('rest_framework.urls', namespace'rest_framework')) #11oct
]

urlpatterns = [
    path('', views.index, name='index'),
]