# question_analytics/urls.py
from django.urls import path
from .views import (
    QuestionAnalyticsListView,
    QuestionAnalyticsCreateView,
    QuestionAnalyticsRetrieveView,
    QuestionAnalyticsUpdateView,
    QuestionAnalyticsDestroyView,
)

urlpatterns = [
    path('question_analytics/', QuestionAnalyticsListView.as_view(), name='question_analytics-list'),
    path('question_analytics/create/', QuestionAnalyticsCreateView.as_view(), name='question_analytics-create'),
    path('question_analytics/<pk>/', QuestionAnalyticsRetrieveView.as_view(), name='question_analytics-detail'),
    path('question_analytics/<pk>/update/', QuestionAnalyticsUpdateView.as_view(), name='question_analytics-update'),
    path('question_analytics/<pk>/delete/', QuestionAnalyticsDestroyView.as_view(), name='question_analytics-delete'),
]
