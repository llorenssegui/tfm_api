from django_rest.quickstart.models import Professor, Assignatura, Curs, Centre, Alumne, Activitat, Qualificacio
from rest_framework import serializers

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class ProfessorResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('nom', 'congnom_1', 'congnom_2', 'email')

class CursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curs
        fields = '__all__'

class AssignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignatura
        fields = '__all__'

class CentreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Centre
        fields = '__all__'

class AlumneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumne
        fields = '__all__'

class ActivitatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activitat
        fields = '__all__'

class QualificacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualificacio
        fields = '__all__'