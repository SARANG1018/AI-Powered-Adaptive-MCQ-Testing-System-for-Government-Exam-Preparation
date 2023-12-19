from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from questions.models import  Questions
from questions.models import  Options

# Create your views here.
@csrf_exempt
# create new question
def CreateQuestions(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_question = Questions.objects.create(question_id=data['question_id'], title=data['title'],attachment=data['attachment'],answer_id=data['answer_id'])
            return JsonResponse({'success': True, 'id': new_question.question_id})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
    #Update the existing question 
def UpdateQuestions(request,question_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            question_to_update = Questions.objects.get(pk=question_id)
            question_to_update.title = data.get('title', question_to_update.title)
            question_to_update.attachment = data.get('attachment', question_to_update.attachment)
            question_to_update.options = data.get('options', question_to_update.options)
            question_to_update.answer_id = data.get('answer_id', question_to_update.answer_id)

            question_to_update.save()
            return JsonResponse({'success': True})
        except Questions.DoesNotExist:
            return JsonResponse({'error': 'Instance not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
            
        
#delete the question 
def DeleteQuestions(request,question_id):
    if request.method == 'DELETE':
        try:
            question_to_delete = Questions.objects.get(pk=question_id)
            question_to_delete.delete()
            return JsonResponse({'success': True})
        except Questions.DoesNotExist:
            return JsonResponse({'error': 'Instance not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)