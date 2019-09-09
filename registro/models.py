from django.db import models

# Create your models here.

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

Class Estudiantes(models.Model)
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)

class Calificaciones(models.Model):
    Calificacion = models.DecimalField(decimal_places=2, max_digits=3)
    Feca = models.DateTimeField('date published')

Class Docentes(models.Model):
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)

    Class Materias(models.Model):
    Materia = models.CharField(max_length=20)