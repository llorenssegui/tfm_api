# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Professor(models.Model):
    nom = models.CharField(max_length=100, blank=True)
    congnom_1 = models.CharField(max_length=100, blank=True)
    congnom_2 = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    data_naixement = models.DateField()
    password = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nom + " " + self.congnom_1

class Centre(models.Model):
    nom = models.CharField(max_length=100, default="")
    ubicacio = models.CharField(max_length=100, default="")
    professor = models.ForeignKey(Professor, related_name='alta', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class AnyAcademic(models.Model):
    anyInici = models.IntegerField(blank=False)
    anyFi = models.IntegerField(blank=False)
    centre = models.ForeignKey(Centre, related_name='anyacademic_centre', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "Any " + self.anyInici + " - " + self.anyFi

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

class Alumne(models.Model):
    nom = models.CharField(max_length=100, blank=True)
    congnom_1 = models.CharField(max_length=100, blank=True)
    congnom_2 = models.CharField(max_length=100, blank=True)
    curs = models.ForeignKey(Curs, related_name='alumne_curs', blank=True, null=True, on_delete=models.CASCADE)
    centre = models.ForeignKey(Centre, related_name='alumne_centre', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom + " " + self.congnom_1

class Assignatura(models.Model):
    nom = models.CharField(max_length=100, blank=True)
    curs = models.ForeignKey(Curs, related_name='assignatura_curs', on_delete=models.CASCADE)
    anyAcademic = models.ForeignKey(AnyAcademic, related_name='assignatura_anyacademic', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Trimestre(models.Model):
    nom = models.CharField(max_length=100, blank=True)
    assignatura = models.ForeignKey(Assignatura, related_name='trimestre_assignatura', blank=True, null=True, on_delete=models.CASCADE)

class Activitat(models.Model):
    nom = nom = models.CharField(max_length=100, blank=True)
    ponderacio = models.IntegerField(default=0)
    avaluable = models.BooleanField(default=True)
    trimestre = models.ForeignKey(Trimestre, related_name='activitat_trimestre', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Qualificacio(models.Model):
    alumne = models.ForeignKey(Alumne, on_delete=models.CASCADE)
    activitat = models.ForeignKey(Activitat, on_delete=models.CASCADE)
    qualificacio = models.IntegerField(default=0)

    def __str__(self):
        return "" + self.qualificacio