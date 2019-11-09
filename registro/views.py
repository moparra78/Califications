from django.shortcuts import render
from rest_framework import serializers, viewsets #11oct

# Create your views here.

from django.http import HttpResponse
from .serializers import FacultadSerializer #11oct
from .serializers import EstudianteSerializer #02nov
from .serializers import DocenteSerializer #02nov
from .models import Facultad #11oct
from .models import Estudiante #02nov
from .models import Docente #02nov

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class FacultadViewSet(viewsets.ModelViewSet): #11oct
    queryset = Facultad.objects.all() #11oct
    serializer_class = FacultadSerializer #11oct
    
class EstudianteViewSet(viewsets.ModelViewSet): #02nov
    queryset = Estudiante.objects.all() #02nov
    serializer_class = EstudianteSerializer #02nov

class DocenteViewSet(viewsets.ModelViewSet): #02nov
    queryset = Docente.objects.all() #02nov
    serializer_class = DocenteSerializer #02nov