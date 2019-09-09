from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Question
from .models import Estudiantes
from .models import Calificaciones
from .models import Docentes
from .models import Materias


admin.site.register(Question)
admin.site.register(Estudiantes)
admin.site.register(Calificaciones)
admin.site.register(Docentes)
admin.site.register(Materias)