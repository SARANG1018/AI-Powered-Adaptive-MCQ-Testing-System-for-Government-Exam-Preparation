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
        fields = ['test_id', 'student_id', 'specialization_id',"accuracy","average_time","test_difficulty" ]

class TestCreateSerializer(serializers.ModelSerializer):
    # student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student',write_only=True)
    # specialization_id = serializers.PrimaryKeyRelatedField(queryset=Specialization.objects.all(), source='specialization',write_only=True)
    student_id_id = serializers.PrimaryKeyRelatedField( read_only=True)
    specialization_id = serializers.PrimaryKeyRelatedField( read_only=True)

    class Meta:
        model = Parakh_Test
        fields = ['test_id', 'student_id_id', 'specialization_id',' average_time','test_difficulty','accuracy']