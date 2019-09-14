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

class Estudiante(models.Model):
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)

class Calificacione(models.Model):
    Calificacion = models.DecimalField(decimal_places=2, max_digits=3)
    Feca = models.DateTimeField('date published')

class Docente(models.Model):
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)

class Materia(models.Model):
    Materia = models.CharField(max_length=20)