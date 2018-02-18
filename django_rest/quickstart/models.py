# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Centre(models.Model):
    nom = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.nom

class Professor(models.Model):
    nom = models.CharField(max_length=100, blank=True)
    congnom_1 = models.CharField(max_length=100, blank=True)
    congnom_2 = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    data_naixement = models.DateField()
    password = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nom + self.congnom_1

class Curs(models.Model):
    ESO = "eso"
    BATXILLERAT = "batxillerat"

    NIVELLS  = {
        (ESO, "ESO"),
        (BATXILLERAT, "Batxillerat"),
    }

    nom = models.CharField(max_length=100, blank=True)
    nivell = models.CharField(max_length=15, choices=NIVELLS, blank=False)

    def __str__(self):
        return self.nom

class Assignatura(models.Model):
    nom = models.CharField(max_length=100, blank=True)
    professor = models.ForeignKey(Professor, related_name='imparteix', on_delete=models.CASCADE)
    curs = models.ForeignKey(Curs, related_name='assignatura_curs', on_delete=models.CASCADE)
    centre = models.ForeignKey(Centre, related_name='assignatura_centre', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Activitat(models.Model):
    nom = nom = models.CharField(max_length=100, blank=True)
    ponderacio = models.IntegerField(default=0)
    avaluable = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

class Alumne(models.Model):
    nom = models.CharField(max_length=100, blank=True)
    congnom_1 = models.CharField(max_length=100, blank=True)
    congnom_2 = models.CharField(max_length=100, blank=True)
    assignatures = models.ManyToManyField(Assignatura, related_name="cursa")
    activitats = models.ManyToManyField(Activitat, related_name="treballa", through="Qualificacio")
    centre = models.ForeignKey(Centre, related_name='alumne_centre', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom + self.congnom_1

class Qualificacio(models.Model):
    alumne = models.ForeignKey(Alumne, on_delete=models.CASCADE)
    activitat = models.ForeignKey(Activitat, on_delete=models.CASCADE)
    qualificacio = models.IntegerField(default=0)

    def __str__(self):
        return "" + self.qualificacio