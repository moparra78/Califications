"""notas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include #11oct
from django.contrib.auth.models import User #11oct
from rest_framework import routers, serializers, viewsets #11oct

from django.contrib import admin
from django.urls import include, path

from registro.views import FacultadViewSet
from registro.views import EstudianteViewSet #02nov
from registro.views import DocenteViewSet #02nov

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter() #11oct
router.register(r'facultad', FacultadViewSet) #11oct
router.register(r'estudiante', EstudianteViewSet) #02nov
router.register(r'docente', DocenteViewSet) #02nov

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('registro/', include('registro.urls')),
    url(r'^', include(router.urls)), #11oct
    #url(r'^api-auth/', include('rest_framework.urls', namespace'rest_framework')), #11oct
]