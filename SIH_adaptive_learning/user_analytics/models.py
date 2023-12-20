from django.db import models
from student.models import Student
from specializations.models import Specialization

# Create your models here.
class User_analysis(models.Model):
    student_id=models.ForeignKey( Student,on_delete=models.CASCADE,related_name="userid",null=True,blank=True)
    user_proficiency=models.DecimalField(decimal_places=2,max_digits=9,default=0.5)
    total_attempts=models.IntegerField(default=0)
    specialization=models.ForeignKey( Specialization,on_delete=models.CASCADE,related_name="user2special",null=True,blank=True)
    accuracy=models.FloatField(default=0,)
    class meta:
        db_table="User_analysis"