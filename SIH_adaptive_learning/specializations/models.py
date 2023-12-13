# specializations/models.py
from django.db import models
from courses.models import Courses

class Specialization(models.Model):
    specialization_id = models.IntegerField(primary_key=True)
    year_of_study = models.DateField()
    specialization_name = models.TextField()
    specialization_syllabus = models.TextField()
    specialization_reference_books = models.TextField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return f"Specialization {self.specialization_id} - {self.specialization_name} (Course: {self.course.courses_name})"
    
    class Meta:
        db_table = 'specializations'
