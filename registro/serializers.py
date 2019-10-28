from rest_framework import serializers, viewsets #11oct

from .models import Facultad
#from polls.models import Facultad


# Serializers define the API representation.
class FacultadSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Facultad
    fields = ['codigo', 'nombre']


