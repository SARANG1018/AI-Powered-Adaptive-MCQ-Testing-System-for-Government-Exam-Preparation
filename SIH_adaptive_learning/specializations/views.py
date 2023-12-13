# specializations/views.py
from rest_framework import generics
from rest_framework import filters
from .models import Specialization
from .serializers import SpecializationSerializer

class SpecializationListView(generics.ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['specialization_id', 'specialization_name', 'course_id__courses_id','year_of_study','specialization_syllabus','specialization_reference_books']

    def get_queryset(self):
        queryset = super().get_queryset()
        # Additional query parameters
        course_id = self.request.query_params.get('course_id', None)
        specialization_id = self.request.query_params.get('specialization_id', None)
        specialization_name = self.request.query_params.get('specialization_name', None)
        year_of_study = self.request.query_params.get('year_of_study', None)
        specialization_syllabus = self.request.query_params.get('specialization_syllabus', None)
        specialization_reference_books = self.request.query_params.get('specialization_reference_books', None)

        if specialization_id:
            queryset = queryset.filter(specialization_id=specialization_id)
        if specialization_name:
            queryset = queryset.filter(specialization_name=specialization_name)
        if year_of_study:
            queryset = queryset.filter(year_of_study=year_of_study)
        if specialization_syllabus:
            queryset = queryset.filter(specialization_syllabus=specialization_syllabus)
        if specialization_reference_books:
            queryset = queryset.filter(specialization_reference_books=specialization_reference_books)
        if course_id:
            queryset = queryset.filter(course_id__courses_id=course_id)
        return queryset

class SpecializationCreateView(generics.CreateAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class SpecializationRetrieveView(generics.RetrieveAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class SpecializationUpdateView(generics.UpdateAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class SpecializationDestroyView(generics.DestroyAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
