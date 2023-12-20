# specializations/serializers.py
from rest_framework import serializers
from courses.models import Courses
from .models import Specialization

class SpecializationSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Courses.objects.all())  # Add this line

    class Meta:
        model = Specialization
        fields = ['specialization_id', 'year_of_study', 'specialization_name', 'specialization_syllabus', 'specialization_reference_books', 'course']
