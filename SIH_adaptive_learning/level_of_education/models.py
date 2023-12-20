# level_of_education/models.py
from django.db import models

class LevelOfEducation(models.Model):
    level_of_education_id = models.BigAutoField(primary_key=True)
    level_of_education_name = models.TextField()

    def __str__(self):
        return f"Level of Education {self.level_of_education_id} - {self.level_of_education_name}"
    class Meta:
        db_table = 'level_of_education'