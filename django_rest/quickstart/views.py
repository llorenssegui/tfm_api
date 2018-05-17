# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta

from django_rest.quickstart.models import Professor, AnyAcademic, Trimestre, Grup, Assignatura, Curs, Centre, Alumne, Activitat, Qualificacio
from rest_framework import viewsets
from django_rest.quickstart.serializers import AnyAcademicSerializer, TrimestreSerializer, CursSerializer, ProfessorResponseSerializer, ProfessorSerializer, AssignaturaSerializer, CentreSerializer, AlumneSerializer, ActivitatSerializer, QualificacioSerializer, GrupSerializer
import jwt

#Views sets
# Create your views here.
class ProfessorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
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

class AnyAcademicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = AnyAcademic.objects.all()
    serializer_class = AnyAcademicSerializer

class TrimestreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Trimestre.objects.all()
    serializer_class = TrimestreSerializer

class GrupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Grup.objects.all()
    serializer_class = GrupSerializer

# Create your views here.
class ProfessorViewList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
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
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        professor = self.get_object(pk)
        serializer = ProfessorSerializer(professor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        professor = self.get_object(pk)
        serializer = ProfessorSerializer(professor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)

        professor = self.get_object(pk)
        serializer = ProfessorSerializer(professor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        professor = self.get_object(pk)
        professor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AssignaturaViewList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        assignatures = Assignatura.objects.all()
        serializer = AssignaturaSerializer(assignatures, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
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
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        assignatura = self.get_object(pk)
        serializer = AssignaturaSerializer(assignatura)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        assignatura = self.get_object(pk)
        serializer = AssignaturaSerializer(assignatura, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        assignatura = self.get_object(pk)
        assignatura.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CursViewList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objectes = Curs.objects.all()
        serializer = CursSerializer(objectes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
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
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        serializer = CursSerializer(objecte)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        serializer = CursSerializer(objecte, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        objecte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CentreViewList(APIView):
    def get(self, request, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objectes = Centre.objects.all()
        serializer = CentreSerializer(objectes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
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
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        serializer = CentreSerializer(objecte)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        serializer = CentreSerializer(objecte, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        objecte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AlumneViewList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        id_centre = request.GET.get("centre", None)
        objectes = None
        if id_centre == None:
            objectes = Alumne.objects.all()
        else:
            objectes = Alumne.objects.filter(centre=id)
        serializer = AlumneSerializer(objectes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
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
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        serializer = AlumneSerializer(objecte)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        serializer = AlumneSerializer(objecte, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        objecte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActivitatViewList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        id_trimestre = id_centre = request.GET.get("trimestre", None)
        objectes = None
        if id_trimestre == None:
            objectes = Activitat.objects.all()
        else:
            objectes = Activitat.objects.filter(trimestre=id_trimestre)
        serializer = ActivitatSerializer(objectes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
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
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        serializer = ActivitatSerializer(objecte)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        serializer = ActivitatSerializer(objecte, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        objecte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LoginView(APIView):

    def post(self, request, format=None):
        rq_email = request.data.get("email", "")
        rq_password = request.data.get("password", "")
        
        jwt_token=None
        professors = Professor.objects.filter(email=rq_email, password=rq_password)
        if professors.count() == 0:
            raise Http404("Usuari no autenticat")
        else :
            timeNow = datetime.utcnow()
            timeExp = timeNow + timedelta(seconds=3600)
            payload = {
                'id': professors.first().id,
                'email': rq_email,
                'exp': timeExp,
            }
            jwt_token = jwt.encode(payload, 'secret', algorithm='HS256')
            if(jwt_token == None):
                raise Http404("Usuari no autenticat")
        serializer = ProfessorResponseSerializer(professors, many=True)
        rsp = {'token': jwt_token, 'professor': serializer.data[0]}
        return Response(rsp)

class AnyAcademicViewList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objectes = AnyAcademic.objects.all()
        serializer = AnyAcademicSerializer(objectes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        serializer = AnyAcademicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnyAcademicViewDetail(APIView):
    def get_object(self, pk):       
        try:
            return AnyAcademic.objects.get(pk=pk)
        except AnyAcademic.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        serializer = AnyAcademicSerializer(objecte)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        serializer = AnyAcademicSerializer(objecte, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        objecte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TrimestreViewList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objectes = Trimestre.objects.all()
        serializer = TrimestreSerializer(objectes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        serializer = TrimestreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrimestreViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Trimestre.objects.get(pk=pk)
        except Trimestre.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        serializer = TrimestreSerializer(objecte)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        serializer = TrimestreSerializer(objecte, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        objecte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GrupViewList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objectes = Grup.objects.all()
        serializer = GrupSerializer(objectes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        serializer = GrupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GrupViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Grup.objects.get(pk=pk)
        except Grup.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        serializer = GrupSerializer(objecte)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        serializer = GrupSerializer(objecte, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        objecte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class QualificacionsViewList(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objectes = Qualificacio.objects.all()
        serializer = QualificacioSerializer(objectes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        serializer = QualificacioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QualificacionsViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Qualificacio.objects.get(pk=pk)
        except Qualificacio.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        serializer = QualificacioSerializer(objecte)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        serializer = QualificacioSerializer(objecte, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            return Response({'error': 'Token is invalid or does not exist'}, status=401)
        
        objecte = self.get_object(pk)
        objecte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

