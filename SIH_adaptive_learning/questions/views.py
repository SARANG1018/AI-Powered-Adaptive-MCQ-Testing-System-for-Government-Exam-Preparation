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
from user_analytics.models import User_analysis
from django.db import transaction


# Create your views here.
# question set
@csrf_exempt
@api_view(['GET'])
def Question_get(request):
    json_data = request.query_params

    analysis,_=User_analysis.objects.get_or_create(student_id=Student.objects.get(student_id=json_data['student_id']),specialization=Specialization.objects.get(specialization_id=json_data["specialization_id"]) if json_data.get("specialization_id",None) != None else None)
    print(analysis.user_proficiency)
    print(analysis.id)
    data=random_question(analysis.user_proficiency)
    return JsonResponse(
        {
            "success": True,
            "data": data,
        }
    )

@csrf_exempt
# create new question
def CreateQuestion(request):
    if request.method == 'POST':
        try:
            question = json.loads(request.body)
            question_obj=Questions.objects.create(id=question["id"],title=question['title'],attachment=question['attachment'])
            special=None

            if(question["specialization"]!=None):
                special=Specialization.objects.filter(specialization_name=question["specialization"])
                if(special==None):
                    special=Specialization.objects.create(specialization_name=question["specialization"])
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
# upload multiple files
def CreateQuestionsMultiple(request):
    if request.method == 'POST':
        try:
            questions = json.loads(request.body)["questions"]
            
            questions_to_be_created=[]
            options_to_be_created=[]
            question_options=[]
            specializations_to_be_created=set()
            for question_data in questions:
                question_obj=Questions(id=question_data["id"],
                    title=question_data['title'],
                    attachment=question_data['attachment'])
                questions_to_be_created.append(question_obj)
                option_array=[]
                for option_data in question_data['options']:
                    option_obj=Options(option_id=option_data['id'],
                        option_title=option_data['option'],
                        option_attachment=option_data['attachment'])
                    options_to_be_created.append(option_obj)
                    option_array.append(option_obj)

                question_options.append(option_array)
                if(question_data["specialization"]!=None):
                    specializations_to_be_created.add(question_data["specialization"])
            specializations_objs=[]
            for i in specializations_to_be_created:
                specializations_objs.append(Specialization(specialization_name=i))

            with transaction.atomic():
                
                Options.objects.bulk_create(options_to_be_created,ignore_conflicts=True)
                Specialization.objects.bulk_create(specializations_objs,ignore_conflicts=True) 
                Questions.objects.bulk_create(questions_to_be_created,ignore_conflicts=True)
                
            for question_obj, option_array in zip(questions_to_be_created, question_options):
                question_obj.options.set(option_array)

                

            return JsonResponse({'success': True, 'message': 'Questions uploaded successfully'})

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
