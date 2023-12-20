# student/urls.py

from django.urls import path
from .views import (
    StudentListView,
    StudentCreateView,
    StudentRetrieveView,
    StudentUpdateView,
    StudentDeleteView,
)

urlpatterns = [
    path('student/', StudentListView.as_view(), name='student-list'),
    path('student/create/', StudentCreateView.as_view(), name='student-create'),
    path('student/<int:pk>/', StudentRetrieveView.as_view(), name='student-retrieve'),
    path('student/<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
]
