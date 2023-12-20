# courses/urls.py
from django.urls import path
from .views import (
    CoursesListView,
    CoursesCreateView,
    CoursesRetrieveView,
    CoursesUpdateView,
    CoursesDestroyView,
)

urlpatterns = [
    path('courses/', CoursesListView.as_view(), name='courses-list'),
    path('courses/create/', CoursesCreateView.as_view(), name='courses-create'),
    path('courses/<int:pk>/', CoursesRetrieveView.as_view(), name='courses-retrieve'),
    path('courses/<int:pk>/update/', CoursesUpdateView.as_view(), name='courses-update'),
    path('courses/<int:pk>/delete/', CoursesDestroyView.as_view(), name='courses-destroy'),
]
