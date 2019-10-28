from django.shortcuts import render
from rest_framework import serializers, viewsets #11oct

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

from .serializers import FacultadSerializer #11oct
from .models import Facultad #11oct

class FacultadViewSet(viewsets.ModelViewSet): #11oct
    queryset = Facultad.objects.all() #11oct
    serializer_class = FacultadSerializer #11oct
    