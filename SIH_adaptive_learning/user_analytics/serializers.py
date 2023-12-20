from rest_framework import serializers
from .models import *
from student.serializers import StudentSerializer
from specializations.serializers import SpecializationSerializer

class UserAnalyticsSerializer(serializers.ModelSerializer):
    Student_id=StudentSerializer(serializers.ModelSerializer)
    Specialization=SpecializationSerializer(serializers.ModelSerializer)
    class Meta:
        model="User_analysis"
        fields = ("student_id","user_proficiency","total_attempts","specialization","accuracy")

