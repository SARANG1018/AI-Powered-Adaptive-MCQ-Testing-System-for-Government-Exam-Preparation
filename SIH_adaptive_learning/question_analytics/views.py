# question_analytics/views.py
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import QuestionAnalytics
from .serializers import QuestionAnalyticsSerializer, QuestionAnalyticsCreateSerializer

class QuestionAnalyticsListView(generics.ListAPIView):
    queryset = QuestionAnalytics.objects.all()
    serializer_class = QuestionAnalyticsSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['question_id', 'total_attempts', 'total_correct', 'difficulty', 'question__title']
    filterset_fields = ['question_id', 'total_attempts', 'total_correct', 'difficulty']

class QuestionAnalyticsCreateView(generics.CreateAPIView):
    queryset = QuestionAnalytics.objects.all()
    serializer_class = QuestionAnalyticsCreateSerializer

class QuestionAnalyticsRetrieveView(generics.RetrieveAPIView):
    queryset = QuestionAnalytics.objects.all()
    serializer_class = QuestionAnalyticsSerializer

class QuestionAnalyticsUpdateView(generics.UpdateAPIView):
    queryset = QuestionAnalytics.objects.all()
    serializer_class = QuestionAnalyticsCreateSerializer

class QuestionAnalyticsDestroyView(generics.DestroyAPIView):
    queryset = QuestionAnalytics.objects.all()
    serializer_class = QuestionAnalyticsSerializer
