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

#Views sets
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

# Create your views here.
class ProfessorViewList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
        professors = Professor.objects.all()
        serializer = ProfessorSerializer(professors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfessorViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Professor.objects.get(pk=pk)
        except Professor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        professor = self.get_object(pk)
        serializer = ProfessorSerializer(professor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        professor = self.get_object(pk)
        serializer = ProfessorSerializer(professor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        professor = self.get_object(pk)
        professor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AssignaturaViewList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
        id_centre = request.GET["centre"]
        assignatures = None
        if(id_centre == None):
            assignatures = Assignatura.objects.filter(centre=int(3))
        else:
            assignatures = Assignatura.objects.filter(centre=int(2))
        serializer = AssignaturaSerializer(assignatures, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AssignaturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignaturaViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Assignatura.objects.get(pk=pk)
        except Assignatura.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        assignatura = self.get_object(pk)
        serializer = AssignaturaSerializer(assignatura)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        assignatura = self.get_object(pk)
        serializer = AssignaturaSerializer(assignatura, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        assignatura = self.get_object(pk)
        assignatura.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CursViewList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
        objectes = Curs.objects.all()
        serializer = CursSerializer(objectes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CursSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CursViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Curs.objects.get(pk=pk)
        except Curs.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objecte = self.get_object(pk)
        serializer = CursSerializer(objecte)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        objecte = self.get_object(pk)
        serializer = CursSerializer(objecte, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        objecte = self.get_object(pk)
        objecte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CentreViewList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
        objectes = Centre.objects.all()
        serializer = CentreSerializer(objectes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CentreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CentreViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Centre.objects.get(pk=pk)
        except Centre.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objecte = self.get_object(pk)
        serializer = CentreSerializer(objecte)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        objecte = self.get_object(pk)
        serializer = CentreSerializer(objecte, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        objecte = self.get_object(pk)
        objecte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AlumneViewList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
        objectes = Alumne.objects.all()
        serializer = AlumneSerializer(objectes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlumneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlumneViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Alumne.objects.get(pk=pk)
        except Alumne.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objecte = self.get_object(pk)
        serializer = AlumneSerializer(objecte)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        objecte = self.get_object(pk)
        serializer = AlumneSerializer(objecte, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        objecte = self.get_object(pk)
        objecte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActivitatViewList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
        objectes = Activitat.objects.all()
        serializer = ActivitatSerializer(objectes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ActivitatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivitatViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Activitat.objects.get(pk=pk)
        except Activitat.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objecte = self.get_object(pk)
        serializer = ActivitatSerializer(objecte)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        objecte = self.get_object(pk)
        serializer = ActivitatSerializer(objecte, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        objecte = self.get_object(pk)
        objecte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

    def get(self, request, format=None):
        rq_id_centre = request.GET['centre']

        assignatures = Assignatura.objects.filter(id=rq_id_centre)
        if assignatures.count() == 0:
            raise Http404("No existeixen assignatures per aquest centre")
        serializer = AssignaturaSerializer(assignatures, many=True)
        return Response(serializer.data)
