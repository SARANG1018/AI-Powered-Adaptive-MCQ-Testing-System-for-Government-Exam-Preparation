# question_analytics/serializers.py
from rest_framework import serializers
from .models import QuestionAnalytics
from questions.serializers import QuestionSerializer
from questions.models import Questions, Options

class QuestionAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnalytics
        fields = ['question_id', 'total_attempts', 'total_correct', 'difficulty']

class QuestionAnalyticsCreateSerializer(serializers.ModelSerializer):
    #question = serializers.PrimaryKeyRelatedField(queryset=Questions.objects.all(), write_only=True)
    
    class Meta:
        model = QuestionAnalytics
        fields = ['question_id', 'total_attempts', 'total_correct', 'difficulty']
