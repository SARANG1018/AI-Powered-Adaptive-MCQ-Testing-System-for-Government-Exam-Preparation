# level_of_education/serializers.py
from rest_framework import serializers
from .models import LevelOfEducation

class LevelOfEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelOfEducation
        fields = ['level_of_education_id', 'level_of_education_name']
