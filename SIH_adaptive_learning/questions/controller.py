from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import QuestionSerializer
from random import sample
import math
from ml_models.algorithms.IRT import next_difficulty_onIRT_3PL, next_ability_onIRT_3PL


def random_question(json):
    try:
        # Get 25 random questions
        all_questions = list(Questions.objects.all())

        random_questions = sample(all_questions, min(25, len(all_questions)))

        # Serialize the questions
        serializer = QuestionSerializer(random_questions, many=True)

        # Return the serialized data
        return serializer.data
    except Exception as e:
        return {"error": str(e)}


def update_question(
    correct_count,  # woh question ko kitno ne sahi kiya hai
    time_required,  # time for that question by current user
    avg_time_for_question,  # avg of all previous attemps
    correct,  # is ans correct or not
    response_count,  # total Question attempts for that question
    user_proficiency,
    difficulty=0.3,
):
    accuracy = correct_count / response_count
    difficulty = next_difficulty_onIRT_3PL(user_proficiency, difficulty)
    return difficulty


# calculate ability_parameter - student skill
# def calculate_ability_parameter(
#     total_responses_of_question, total_question_count, num_options=4
# ):
#     try:
#         return math.log(
#             sum(total_responses_of_question)
#             / (num_options * total_question_count)
#             / (
#                 1
#                 - sum(total_responses_of_question)
#                 / (num_options * total_question_count)
#             )
#         )
#     except:
#         if sum(total_responses_of_question) == 0:
#             return -4
#         else:
#             return 4


def update_user_proficiency(user_proficiency, ability_of_student):
    ability_of_student = next_ability_onIRT_3PL(user_proficiency, ability_of_student)



def generate_questions(
    num_questions, questions, user_proficiency, assigned_questions, kmeans_clusters
):
    distances = {}

    # Calculate distances between user proficiency and question difficulties
    for question_id, difficulty in questions.items():
        distance = abs(difficulty - user_proficiency)
        distances[question_id] = distance

    # Sort questions based on distances
    sorted_questions = sorted(distances.keys(), key=lambda x: distances[x])

    # Filter out questions that have already been assigned
    available_questions = [q for q in sorted_questions if q not in assigned_questions]

    # Select new questions for the user
    selected_questions = available_questions[:num_questions]

    # Update the list of assigned questions
    assigned_questions.extend(selected_questions)

    return selected_questions


# def generate_questions(
#     num_questions,  # Total Questions to be generated in next set
#     questions: dict,  # Difficulties of all Questions on specialization
#     user_proficiency,
# ):

#     distances =dict()

#     for id,difficulty in questions.values():
#         distance= difficulty-user_proficiency
#         distances.append(id, distance)

#     questions_set=sorted(distances.keys(),key=lambda x: abs(distances.get(x)))
#     return questions_set[:25]


# import random

# # calculate lesson_difficulty
# def calculate_lesson_difficulty(
#     correct_responses,  # total User ka us set mein  kitna correct hai
#     total_questions_in_lesson_set: int
#     # Total Question in previous set
# ):
#     try:
#         return math.log(
#             (1 - (sum(correct_responses) / total_questions_in_lesson_set))
#             / (sum(correct_responses) / total_questions_in_lesson_set)
#         )
#     except:
#         if all(response == 0 for response in correct_responses):
#             return 4
#         else:
#             return -4


# # calculating correctness_prob
# def calculate_correctness_prob(ability_parameter, lesson_difficulty):
#     return ((math.e) ** (ability_parameter - lesson_difficulty)) / (
#         1 + (math.e) ** (ability_parameter - lesson_difficulty)
#     )
