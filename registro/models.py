from django.db import models

# Create your models here.

from django.db import models


#class Question(models.Model):
    #question_text = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')


#class Choice(models.Model):
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #choice_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)

class Facultad(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)

class Docente(models.Model):
    facultad = models.ForeignKey(Facultad, null=True, on_delete=models.CASCADE)
    codigo = models.CharField(default=1, max_length=20)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    honorarios = models.IntegerField(default=0)

class Materia(models.Model):
    docente = models.ForeignKey(Docente, null=True, on_delete=models.CASCADE)
    facultad = models.ForeignKey(Facultad, null=True, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    
class Estudiante(models.Model):
    materia = models.ManyToManyField(Materia)
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    acudiente = models.CharField(default=' ', max_length=20)

class Calificacione(models.Model):
    estudiante = models.ForeignKey(Estudiante, null=True, on_delete=models.CASCADE)
    calificacion = models.DecimalField(decimal_places=2, max_digits=3)
    fecha = models.DateTimeField('date published')

