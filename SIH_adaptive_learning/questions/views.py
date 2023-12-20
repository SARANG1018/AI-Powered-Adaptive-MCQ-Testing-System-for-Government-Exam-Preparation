from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from questions.models import  Questions
from questions.models import  Options
from .controller import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser


# Create your views here.
# question set
@csrf_exempt
@api_view(("POST",))
@parser_classes([JSONParser])
def Question_get(request):
    data=random_question(request.data)
    return JsonResponse(
        {
            "success": True,
            "data": data,
        }
    )

@csrf_exempt
# create new question
def CreateQuestions(request):
    if request.method == 'POST':
        try:
            question = json.loads(request.body)
            question_obj=Questions.objects.create(id=question["id"],title=question['title'],specialization=question["specialization"],attachment=question['attachment'])
            for option in question['options']:
                option_obj=Options.objects.create(option_id=option['id'],option_title=option['option'],option_attachment=option['attachment'])
                option_obj.save()
                question_obj.options.add(option_obj)
            if(question.get("answer_id")!=None):
                question_obj["answer"]=Options.objects.get(question["answer_id"])
                question_obj.save()
            return JsonResponse({'success': True, 'id':question_obj.id})

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})        
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
    #Update the existing question 
def UpdateQuestions(request,id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            question = Questions.objects.get(pk=id)
            question.title = data.get('title', question.title)
            question.attachment = data.get('attachment', question.attachment)
            question_options = data.get('options', [])
            question.options.clear()  # Clear existing options
            for option_data in question_options:
                option, created = Options.objects.get_or_create(
                    option_id=option_data.get('id', ''),
                    defaults={
                        'option_title': option_data.get('option', ''),
                        'option_attachment': option_data.get('attachment', ''),
                    }
                )
                question.options.add(option)
            question.answer_id = data.get('answer_id', question.answer_id)

            question.save()
            return JsonResponse({'success': True})
        except Questions.DoesNotExist:
            return JsonResponse({'error': 'Instance not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
            
        
#delete the question 
@csrf_exempt
def DeleteQuestions(request,id):
    if request.method == 'DELETE':
        try:
            question_to_delete = Questions.objects.get(pk=id)
            question_to_delete.delete()
            return JsonResponse({'success': True})
        except Questions.DoesNotExist:
            return JsonResponse({'error': 'Instance not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    

# calculation level of questions
# def level_question(request,id):
#     data = json.loads(request.body)
#     question = Questions.objects.get(pk=id)
#     question.= data.get('title', question.title)
