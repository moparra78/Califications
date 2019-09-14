from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Question
from .models import Estudiante
from .models import Calificacione
from .models import Docente
from .models import Materia


admin.site.register(Question)
admin.site.register(Estudiante)
admin.site.register(Calificacione)
admin.site.register(Docente)
admin.site.register(Materia)