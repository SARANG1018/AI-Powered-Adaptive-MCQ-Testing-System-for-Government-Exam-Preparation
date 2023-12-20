# courses/serializers.py
from rest_framework import serializers
from .models import Courses

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['courses_id', 'courses_name', 'level']
