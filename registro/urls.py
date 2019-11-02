from django.urls import path
from django.conf.urls import url, include #11oct
from django.contrib.auth.models import User #11oct
from rest_framework import routers, serializers, viewsets #11oct

from . import views
from registro.views import FacultadViewSet #11oct

from django.contrib import admin
from django.urls import include, path

