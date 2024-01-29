# test/urls.py
from django.urls import path
from .views import (
    TestListView,
    create_test,
    TestRetrieveView,
    TestUpdateView,
    TestDestroyView,
)

urlpatterns = [
    path('tests', TestListView.as_view(), name='test-list'),
    path('tests/create/', create_test, name='test-create'),
    path('tests/<int:pk>/', TestRetrieveView.as_view(), name='test-retrieve'),
    path('tests/<int:pk>/update/', TestUpdateView.as_view(), name='test-update'),
    path('tests/<int:pk>/delete/', TestDestroyView.as_view(), name='test-destroy'),
]
