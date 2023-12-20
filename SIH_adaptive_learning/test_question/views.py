from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from parakh_test.models import Parakh_Test
from specializations.models import Specialization
from student.models import Student
from django.http import JsonResponse
from ml_models.algorithms.IRT import next_ability_onIRT_3PL,next_difficulty_onIRT_3PL
from user_analytics.models import User_analysis
from parakh_test.serializers import TestSerializer
# Create your views here.
def load_json_from_request(request):
    import json

    return json.loads(request.body.decode("utf-8"))


@csrf_exempt
def question_attempt(request):
    json_data = load_json_from_request(request)
    current_question = Questions.objects.filter(
        id=json_data["id"]
    ).first()
    correct = None
    # print(current_question["answer_id"])
    if current_question.answer.id != None:
        correct = current_question.answer.id == json_data["selected_option_id"]
    TestQestions.objects.create(
        time_required=json_data["time_required"],
        option_marked=Options.objects.get(id=json_data["selected_option_id"]),
        question=Questions.objects.get(id=json_data["question"]),
        assignment=json_data["assignment"],
        user=json_data["user"],
     
        correct=correct,
    )
    # return JsonResponse({"success": True}, status=200)

    # def test_questions(request,number_questions):
    #     for number in number_questions:
    #         question_attempt(request)


from django.core.serializers.json import DjangoJSONEncoder
from django.db import models


@csrf_exempt
def test_attempt(request):
    json_data = load_json_from_request(request)
    specialization=Specialization.objects.get(specialization_id=json_data["specialization_id"]) if json_data["specialization_id"] != None else None
    all_test_question_attempts=[]
    student=Student.objects.get(student_id=json_data["student_id"])
    user_analytics,_=User_analysis.objects.get_or_create(student_id=student,specialization=specialization)
    current_user_proficiency=user_analytics.user_proficiency
    
    test_obj = Parakh_Test.objects.create(
        test_id=json_data["test_id"],
        student_id=student,
        specialization_id=specialization,
    )
    total_questions = len(json_data["attempts"])
    correct_questions = 0
    total_time = 0

    for question in json_data["attempts"]:
        current_question = Questions.objects.filter(
            id=question["question_id"]
        ).first()
        correct = None
        test_difficulty=0
        current_question_difficulty=current_question.difficulty
        if current_question.answer_id != None:
            correct = current_question.answer_id.id == question["selected_option_id"]
        all_test_question_attempts.append(
            TestQestions(
                time_required=question["time_required"],
                option_marked=Options.objects.get(option_id=question["selected_option_id"]),
                question=current_question,
                student=student,
                correct=correct,
                test_attempted=test_obj,
            )
        )
        total_time += question["time_required"]
        if correct:
            correct_questions += 1
        current_user_proficiency=next_ability_onIRT_3PL(float(current_user_proficiency),float(current_question_difficulty))
        current_question_difficulty=next_difficulty_onIRT_3PL(float(current_user_proficiency),float(current_question_difficulty))
        current_question.difficulty=current_question_difficulty
        current_question.save()
        test_difficulty+=current_question_difficulty


    accuracy = correct_questions / total_questions
    average_time = total_time / total_questions
    test_score=correct_questions


    test_obj.accuracy = accuracy
    test_obj.average_time = average_time
    test_obj.test_score=test_score
    test_obj.test_difficulty=test_difficulty/total_questions
    user_analytics.user_proficiency=current_user_proficiency
    user_analytics.save()
    test_obj.save()
    TestQestions.objects.bulk_create(all_test_question_attempts)
    return JsonResponse({"success": True,"results":TestSerializer(test_obj).data}, status=200)

