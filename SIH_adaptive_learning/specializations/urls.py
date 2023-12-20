# specializations/urls.py
from django.urls import path
from .views import (
    SpecializationListView,
    SpecializationCreateView,
    SpecializationRetrieveView,
    SpecializationUpdateView,
    SpecializationDestroyView,
)

urlpatterns = [
    path('specializations/', SpecializationListView.as_view(), name='specialization-list'),
    path('specializations/create/', SpecializationCreateView.as_view(), name='specialization-create'),
    path('specializations/<int:pk>/', SpecializationRetrieveView.as_view(), name='specialization-retrieve'),
    path('specializations/<int:pk>/update/', SpecializationUpdateView.as_view(), name='specialization-update'),
    path('specializations/<int:pk>/delete/', SpecializationDestroyView.as_view(), name='specialization-destroy'),
]
