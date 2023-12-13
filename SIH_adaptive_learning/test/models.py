# test/models.py
from django.db import models
from student.models import Student
from specializations.models import Specialization

class Test(models.Model):
    test_id = models.IntegerField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    specialization_id = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"Test {self.test_id} - Student: {self.student_id.student_name}, Specialization: {self.specialization_id.specialization_name}, Date: {self.date}"
