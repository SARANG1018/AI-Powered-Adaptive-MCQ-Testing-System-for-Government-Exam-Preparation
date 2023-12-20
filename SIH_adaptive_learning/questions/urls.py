from django.urls import path
from .views import CreateQuestion, UpdateQuestions, DeleteQuestions,Question_get, CreateQuestionsMultiple

urlpatterns = [
    # path("upload_questions/", views.upload_questions_from_json_api),
    path('create', CreateQuestion, name='create_questions'),
    path('createMultiple', CreateQuestionsMultiple, name='create_questions_m'),
    path('get_questions', Question_get, name='create_questions'),
    path('update/<int:id>', UpdateQuestions, name='update_questions'),
    path('delete/<int:id>', DeleteQuestions, name='delete_questions'),
]