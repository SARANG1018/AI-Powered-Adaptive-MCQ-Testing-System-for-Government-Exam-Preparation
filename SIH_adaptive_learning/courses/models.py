# courses/models.py
from django.db import models
from level_of_education.models import LevelOfEducation

class Courses(models.Model):
    courses_id = models.IntegerField(primary_key=True)
    courses_name = models.CharField(max_length=255)
    level = models.ForeignKey(LevelOfEducation, on_delete=models.CASCADE)

    def __str__(self):
        return f"Courses {self.courses_id} - {self.courses_name} (Level: {self.level.level_of_education_name})"
    class Meta:
        db_table = 'courses'