# courses/views.py
from rest_framework import generics
from rest_framework import filters
from .models import Courses
from .serializers import CoursesSerializer

class CoursesListView(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['courses_id', 'courses_name', 'level__level_of_education_id']

    def get_queryset(self):
        queryset = super().get_queryset()
        # Additional query parameters
        course_id = self.request.query_params.get('course_id', None)
        course_name= self.request.query_params.get('course_name', None)
        level_id = self.request.query_params.get('level_id', None) 
        
        if course_id:
            queryset = queryset.filter(courses_id=course_id)
        if course_name:
            queryset = queryset.filter(courses_name__icontains=course_name)
        if level_id:
            queryset = queryset.filter(level__level_of_education_id=level_id)
        
        return queryset

class CoursesCreateView(generics.CreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

class CoursesRetrieveView(generics.RetrieveAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

class CoursesUpdateView(generics.UpdateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

class CoursesDestroyView(generics.DestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
