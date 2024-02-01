from django.urls import path
from . import views

urlpatterns =[
    path("question_attempt", views.question_attempt),
    path("test_attempt", views.test_attempt),
    path("get_question_attempt", views.get_question_attempt)
]