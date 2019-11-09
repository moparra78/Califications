from rest_framework import serializers, viewsets #11oct

from .models import Facultad
from .models import Estudiante #02nov
from .models import Docente #02nov
#from polls.models import Facultad


# Serializers define the API representation.
class FacultadSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Facultad
    fields = ['codigo', 'nombre']

class EstudianteSerializer(serializers.HyperlinkedModelSerializer): #02nov
  class Meta: #02nov
    model = Estudiante #02nov
    fields = ['id','codigo', 'nombre', 'apellido', 'email', 'direccion', 'telefono', 'acudiente'] #02nov

class DocenteSerializer(serializers.HyperlinkedModelSerializer): #02nov
  class Meta: #02nov
    model = Docente #02nov
    fields = ['id','codigo', 'nombre', 'apellido', 'email', 'honorarios'] #02nov