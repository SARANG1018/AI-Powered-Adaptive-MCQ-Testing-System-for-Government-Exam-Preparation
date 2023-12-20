# test/models.py
from django.db import models
from student.models import Student
from specializations.models import Specialization

class Parakh_Test(models.Model):
    test_id = models.IntegerField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    specialization_id = models.ForeignKey(Specialization, on_delete=models.CASCADE,null=True)
   
    average_time=models.FloatField(null=True,blank=True)
    test_difficulty=models.FloatField(null=True,blank=True)     #test_difficulty(lesson_difficulty) 
    accuracy=models.FloatField(null=True,blank=True)


    def __str__(self):
        return f"Test {self.test_id} - Student: {self.student_id.student_name}, Specialization: {self.specialization_id.specialization_name}, Date: {self.date}"
    
    class Meta: 
        db_table = 'parakh_test'