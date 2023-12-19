# question_analytics/models.py
from django.db import models
from questions.models import Questions

class QuestionAnalytics(models.Model):
    question_id = models.TextField(primary_key=True, db_index=True)
    total_attempts = models.BigIntegerField()
    total_correct = models.BigIntegerField()
    difficulty = models.FloatField()
    #question = models.ForeignKey(Questions, on_delete=models.CASCADE)

    def __str__(self):
        return f"QuestionAnalytics {self.question_id} - Attempts: {self.total_attempts}, Correct: {self.total_correct}, Difficulty: {self.difficulty}"

    class Meta:
        db_table = 'question_analytics'
