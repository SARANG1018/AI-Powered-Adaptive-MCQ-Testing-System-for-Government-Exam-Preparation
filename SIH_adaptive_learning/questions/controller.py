from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import * 
import json
import random
from .serializers import QuestionSerializer
from random import sample

def random_question(request):
    
        try:
            # Get 25 random questions
            all_questions = list(Questions.objects.all())
            random_questions = sample(all_questions, min(25, len(all_questions)))

            
            # Serialize the questions
            serializer = QuestionSerializer(random_questions, many=True)
            
            # Return the serialized data
            return serializer.data
        except Exception as e:
            return {'error': str(e)}
    