# specializations/models.py
from django.db import models
from courses.models import Courses

class Specialization(models.Model):
    specialization_id = models.BigAutoField(primary_key=True)
    year_of_study = models.DateField(null=True,blank=True)
    specialization_name = models.TextField(null=True, blank=True)
    specialization_syllabus = models.TextField(null=True, blank=True)
    specialization_reference_books = models.TextField(null=True,blank=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"Specialization {self.specialization_id} - {self.specialization_name} (Course: {self.course.courses_name})"
    
    class Meta:
        db_table = 'specializations'
