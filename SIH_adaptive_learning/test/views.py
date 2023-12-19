# test/views.py
from rest_framework import generics
from rest_framework import filters
from .models import Test
from .serializers import TestCreateSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from specializations.models import Specialization
from student.models import Student
class TestListView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestCreateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['test_id', 'student_id__student_id', 'specialization_id__specialization_id', 'date']

    def get_queryset(self):
        queryset = super().get_queryset()
        # Additional query parameters
        test_id = self.request.query_params.get('test_id', None)
        date = self.request.query_params.get('date', None)
        student_id = self.request.query_params.get('student_id', None)
        specialization_id = self.request.query_params.get('specialization_id', None)
        if test_id:
            queryset = queryset.filter(test_id=test_id)
        if date:    
            queryset = queryset.filter(date=date)
        if student_id:
            queryset = queryset.filter(student_id__student_id=student_id)
        if specialization_id:
            queryset = queryset.filter(specialization_id__specialization_id=specialization_id)
        return queryset
@csrf_exempt
def create_test(request):
    import json
    if request.method == 'POST':
        json_data=json.loads(request.body)
        test_id = json_data['test_id']
        student_id = Student.objects.get(student_id=json_data['student_id'])
        specialization_id = Specialization.objects.get(specialization_id=json_data['specialization_id'])
        date = json_data['date']

        test = Test(test_id=test_id, student_id=student_id, specialization_id=specialization_id, date=date)
        test.save()
        return HttpResponse("Test created successfully")

    else:
        return HttpResponse("Error creating test")

class TestRetrieveView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestCreateSerializer

class TestUpdateView(generics.UpdateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestCreateSerializer

class TestDestroyView(generics.DestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestCreateSerializer