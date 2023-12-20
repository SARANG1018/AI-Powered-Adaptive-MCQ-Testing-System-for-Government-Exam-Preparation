from rest_framework import serializers
from .models import *

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Options
        fields=["option_id","option_title","option_attachment"]

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, required=False)
    class Meta:
        model = Questions
        fields = ["id", "title", "options", "attachment", "specialization"]