from django.db import models
from student.models import Student
from specializations.models import Specialization

# Create your models here.
class User_analysis(models.Model):
    student_id=models.ForeignKey( Student,on_delete=models.CASCADE,related_name="userid",null=True,blank=True)
    user_proficiency=models.TextField(null=True, blank=True)
    total_attempts=models.TextField(null=True, blank=True)
    specialization=models.ForeignKey( Specialization,on_delete=models.CASCADE,related_name="user2special",null=True,blank=True)
    accuracy=models.TextField(null=True, blank=True)
    class meta:
        db_table="User_analysis"