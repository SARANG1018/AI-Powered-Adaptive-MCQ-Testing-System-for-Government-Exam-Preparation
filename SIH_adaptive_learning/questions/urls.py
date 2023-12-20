from django.urls import path
<<<<<<< HEAD
from .views import CreateQuestions, UpdateQuestions, DeleteQuestions,Question_get
=======
from .views import CreateQuestions, UpdateQuestions, DeleteQuestions,Question_get, CreateQuestionsMultiple
>>>>>>> 335dd2464cdd8e13d40babf5f3fcbb8a822c1c2a

urlpatterns = [
    # path("upload_questions/", views.upload_questions_from_json_api),
    path('create/', CreateQuestions, name='create_questions'),
<<<<<<< HEAD
=======
    path('createMultiple/', CreateQuestionsMultiple, name='create_questions_m'),
>>>>>>> 335dd2464cdd8e13d40babf5f3fcbb8a822c1c2a
    path('get_question/', Question_get, name='create_questions'),
    path('update/<int:id>/', UpdateQuestions, name='update_questions'),
    path('delete/<int:id>/', DeleteQuestions, name='delete_questions'),
]