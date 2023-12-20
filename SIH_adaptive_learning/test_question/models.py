from django.db import models
from questions.models import Questions
from questions.models import Options
from parakh_test.models import Parakh_Test
from student.models import Student

# Create your models here.

class TestQestions(models.Model):
    id=models.BigAutoField(primary_key=True) 
    time_required=models.BigIntegerField(null=True,blank=True)
    # question id
    question=models.ForeignKey(Questions,related_name="parakh_test_question_attempted",on_delete=models.CASCADE)
    # option marked by student
    option_marked=models.ForeignKey(Options,null=True,blank=True,related_name="parakh_test_marked_answer",on_delete=models.CASCADE)
    # test id
    test_attempted=models.ForeignKey( Parakh_Test,on_delete=models.CASCADE,related_name="test2user",null=True,blank=True)
    #student id
    student=models.ForeignKey( Student,on_delete=models.CASCADE,related_name="iduser",null=True,blank=True)
    # whether the answer is correct or incorrect
    correct=models.BooleanField(null=True,blank=True)
   
    class meta:
        db_table="Test_Question"
