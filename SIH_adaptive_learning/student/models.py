# student/models.py
from django.db import models

class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=50)

    def __str__(self):
        return self.student_name
    class Meta:
        db_table = 'student'