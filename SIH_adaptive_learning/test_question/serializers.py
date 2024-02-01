from rest_framework import serializers
from .models import *
from questions.serializers import QuestionSerializer
from questions.serializers import OptionSerializer
from .models import TestQestions

class TestQuestionSerializer(serializers.ModelSerializer):
    question=QuestionSerializer( required=False)
    option_marked=OptionSerializer(required=False)
    class Meta:
        model=TestQestions
        fields=["id","time_required","question","option_marked","test_attempted","student","correct"]