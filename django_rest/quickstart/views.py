# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django_rest.quickstart.models import Professor, Assignatura, Curs, Centre, Alumne, Activitat, Qualificacio
from rest_framework import viewsets
from django_rest.quickstart.serializers import CursSerializer, ProfessorResponseSerializer, ProfessorSerializer, AssignaturaSerializer, CentreSerializer, AlumneSerializer, ActivitatSerializer, QualificacioSerializer

# Create your views here.
class ProfessorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class CursViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Curs.objects.all()
    serializer_class = CursSerializer

class AssignaturaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Assignatura.objects.all()
    serializer_class = AssignaturaSerializer

class CentreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Centre.objects.all()
    serializer_class = CentreSerializer

class AlumneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Alumne.objects.all()
    serializer_class = AlumneSerializer

class ActivitatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Activitat.objects.all()
    serializer_class = ActivitatSerializer

class QualificacioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Qualificacio.objects.all()
    serializer_class = QualificacioSerializer


class LoginView(APIView):

    def post(self, request, format=None):
        rq_email = request.data.get("email", "")
        rq_password = request.data.get("password", "")
        
        professors = Professor.objects.filter(email=rq_email, password=rq_password)
        if professors.count() == 0:
            raise Http404("Usuari no autenticat")
        serializer = ProfessorResponseSerializer(professors, many=True)
        return Response(serializer.data)

class AssignaturesView(APIView):

    def get(self, request, centre=None):
        rq_id_centre = centre

        assignatures = Assignatura.objects.filter(id=rq_id_centre)
        if assignatures.count() == 0:
            raise Http404("No existeixen assignatures per aquest centre")
        serializer = AssignaturaSerializer(assignatures, many=True)
        return Response(serializer.data)
