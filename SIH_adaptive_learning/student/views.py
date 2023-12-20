# student/views.py

from rest_framework import generics
from rest_framework import filters
from .models import Student
from .serializers import StudentSerializer

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['student_name', 'student_id']

    def get_queryset(self):
        queryset = super().get_queryset()
        student_id_param = self.request.query_params.get('student_id', None)
        student_name_param = self.request.query_params.get('student_name', None)

        if student_id_param:
            queryset = queryset.filter(student_id=student_id_param)
        if student_name_param:
            queryset = queryset.filter(student_name__icontains=student_name_param)

        return queryset

class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def perform_create(self, serializer):
        # Extract student_id from request data, default to None if not provided
        student_id = self.request.data.get('student_id', None)
        serializer.save(student_id=student_id)

class StudentRetrieveView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDeleteView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
