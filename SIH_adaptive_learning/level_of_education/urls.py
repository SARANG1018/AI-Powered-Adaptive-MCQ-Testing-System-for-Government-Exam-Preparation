# level_of_education/urls.py
from django.urls import path
from .views import (
    LevelOfEducationListView,
    LevelOfEducationCreateView,
    LevelOfEducationRetrieveView,
    LevelOfEducationUpdateView,
    LevelOfEducationDestroyView,
)

urlpatterns = [
    path('levels/', LevelOfEducationListView.as_view(), name='level-list'),
    path('levels/create/', LevelOfEducationCreateView.as_view(), name='level-create'),
    path('levels/<int:pk>/', LevelOfEducationRetrieveView.as_view(), name='level-retrieve'),
    path('levels/<int:pk>/update/', LevelOfEducationUpdateView.as_view(), name='level-update'),
    path('levels/<int:pk>/delete/', LevelOfEducationDestroyView.as_view(), name='level-destroy'),
]
