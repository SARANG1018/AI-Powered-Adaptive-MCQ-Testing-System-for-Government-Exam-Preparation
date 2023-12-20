from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *

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
        average_time=json_data["average_time"],
        accuracy=json_data["accuracy"],
        test_difficulty=json_data["test_difficulty"],
        correct=correct,
    )
    # return JsonResponse({"success": True}, status=200)

    # def test_questions(request,number_questions):
    #     for number in number_questions:
    #         question_attempt(request)


