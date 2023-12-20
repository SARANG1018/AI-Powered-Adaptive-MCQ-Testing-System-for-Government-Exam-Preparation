from django.urls import path
from .views import CreateQuestions, UpdateQuestions, DeleteQuestions,Question_get

urlpatterns = [
    # path("upload_questions/", views.upload_questions_from_json_api),
    path('create/', CreateQuestions, name='create_questions'),
    path('createMultiple/', CreateQuestions, name='create_questions'),
    path('get_question/', Question_get, name='create_questions'),
    path('update/<int:id>/', UpdateQuestions, name='update_questions'),
    path('delete/<int:id>/', DeleteQuestions, name='delete_questions'),
]