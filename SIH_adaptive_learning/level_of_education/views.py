# level_of_education/views.py
from rest_framework import generics
from rest_framework import filters
from .models import LevelOfEducation
from .serializers import LevelOfEducationSerializer

class LevelOfEducationListView(generics.ListAPIView):
    queryset = LevelOfEducation.objects.all()
    serializer_class = LevelOfEducationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['level_of_education_id', 'level_of_education_name']

    def get_queryset(self):
        queryset = super().get_queryset()
        # Additional query parameters
        level_id = self.request.query_params.get('level_id', None)
        level_name = self.request.query_params.get('level_name', None)
        if level_id:
            queryset = queryset.filter(level_of_education_id=level_id)
        if level_name:  
            queryset = queryset.filter(level_of_education_name__icontains=level_name)
        return queryset

class LevelOfEducationCreateView(generics.CreateAPIView):
    queryset = LevelOfEducation.objects.all()
    serializer_class = LevelOfEducationSerializer

class LevelOfEducationRetrieveView(generics.RetrieveAPIView):
    queryset = LevelOfEducation.objects.all()
    serializer_class = LevelOfEducationSerializer

class LevelOfEducationUpdateView(generics.UpdateAPIView):
    queryset = LevelOfEducation.objects.all()
    serializer_class = LevelOfEducationSerializer

class LevelOfEducationDestroyView(generics.DestroyAPIView):
    queryset = LevelOfEducation.objects.all()
    serializer_class = LevelOfEducationSerializer
