from django.urls import path
from . import views

urlpatterns =[
    path("question_attempt", views.question_attempt),
    path("test_attempt", views.test_attempt)
]