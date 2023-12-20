from rest_framework import serializers
from .models import *
from questions.serializers import QuestionSerializer
from questions.serializers import OptionSerializer

class TestQuestionSerializer(serializers.Serializer):
    question=QuestionSerializer(many=True, required=False)
    question=OptionSerializer(many=True, required=False)
    class meta:
        model="Test_Question"
        fields={"id","time_required","question","option_marked","assignment_id","user_id","correct","average_time","accuracy","test_difficulty"}