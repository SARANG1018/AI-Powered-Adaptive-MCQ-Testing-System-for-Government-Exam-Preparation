# specializations/urls.py
from django.urls import path
from .views import CreateQuestions, UpdateQuestions, DeleteQuestions

urlpatterns = [
    path('create/', CreateQuestions, name='create_questions'),
    path('update/<int:question_id>/', UpdateQuestions, name='update_questions'),
    path('delete/<int:question_id>/', DeleteQuestions, name='delete_questions'),
]