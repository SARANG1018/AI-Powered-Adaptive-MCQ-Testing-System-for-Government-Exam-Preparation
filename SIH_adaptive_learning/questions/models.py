from django.db import models

# Create your models here.
class Options(models.Model):
    option_id=models.TextField(primary_key=True)
    option_title=models.TextField(null=True,blank=True)
    option_attachment=models.TextField(null=True, blank=True)



class Questions(models.Model):
    question_id = models.TextField(primary_key=True)
    title = models.TextField(null=True,blank=True)
    attachment=models.TextField(null=True, blank=True)
    options=models.ManyToManyField(Options, blank=True)
    answer_id = models.ForeignKey(Options,on_delete=models.CASCADE,related_name="question2option",null=True,blank=True)
