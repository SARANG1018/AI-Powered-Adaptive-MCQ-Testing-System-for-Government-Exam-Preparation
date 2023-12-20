from django.db import models
from specializations.models import Specialization

# Create your models here.
class Options(models.Model):
    option_id=models.TextField(primary_key=True)
    option_title=models.TextField(null=True,blank=True)
    option_attachment=models.TextField(null=True, blank=True)
    class Meta:
        db_table = "options"


class Questions(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField(null=True,blank=True)
    attachment=models.TextField(null=True, blank=True)
    options=models.ManyToManyField(Options, blank=True)
    answer_id = models.ForeignKey(Options,on_delete=models.CASCADE,related_name="question2option",null=True,blank=True)
    specialization=models.ForeignKey( Specialization,on_delete=models.CASCADE,related_name="ques2special",null=True,blank=True)
    class Meta:
        db_table = "questions"

