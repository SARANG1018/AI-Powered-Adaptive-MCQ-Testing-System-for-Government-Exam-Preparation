# test/serializers.py
from rest_framework import serializers
from .models import Parakh_Test
from student.serializers import StudentSerializer
from specializations.serializers import SpecializationSerializer
from student.models import Student
from specializations.models import Specialization
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parakh_Test
        fields = ['test_id', 'student_id', 'specialization_id', 'date']

class TestCreateSerializer(serializers.ModelSerializer):
    # student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student',write_only=True)
    # specialization_id = serializers.PrimaryKeyRelatedField(queryset=Specialization.objects.all(), source='specialization',write_only=True)
    student = serializers.PrimaryKeyRelatedField( read_only=True)
    specialization = serializers.PrimaryKeyRelatedField( read_only=True)

    class Meta:
        model = Parakh_Test
        fields = ['test_id', 'student', 'specialization', 'date']