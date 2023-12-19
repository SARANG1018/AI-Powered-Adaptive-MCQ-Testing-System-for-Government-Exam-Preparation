from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import random
from .serializers import QuestionSerializer
from random import sample
import math


def random_question(json):
    try:
        # Get 25 random questions
        all_questions = list(Questions.objects.all())
        Questions.objects.get

        random_questions = sample(all_questions, min(25, len(all_questions)))

        # Serialize the questions
        serializer = QuestionSerializer(random_questions, many=True)

        # Return the serialized data
        return serializer.data
    except Exception as e:
        return {"error": str(e)}


# calculate ability_parameter - student skill
def calculate_ability_parameter(
    total_responses_of_question, total_question_count, num_options=4
):
    try:
        return math.log(
            sum(total_responses_of_question)
            / (num_options * total_question_count)
            / (
                1
                - sum(total_responses_of_question)
                / (num_options * total_question_count)
            )
        )
    except:
        if sum(total_responses_of_question) == 0:
            return -4
        else:
            return 4


def update_question(
    correct_count,  # woh question ko kitno ne sahi kiya hai
    time_required,  # time for that question by current user
    avg_time_for_question,  # avg of all previous attemps
    correct,  # is ans correct or not
    response_count,  # total Question attempts for that question
    difficulty=0.3,
):
    accuracy = correct_count / response_count

    if correct:
        # Increase difficulty when the answer is correct
        difficulty += 0.1 * (time_required / avg_time_for_question) * accuracy
    else:
        # Decrease difficulty when the answer is incorrect
        difficulty -= 0.1 * (time_required / avg_time_for_question) * accuracy

    return difficulty

import random


# calculate lesson_difficulty
def calculate_lesson_difficulty(
    correct_responses,  # total User ka us set mein  kitna correct hai
    total_questions_in_lesson_set: int
    # Total Question in previous set
):
    try:
        return math.log(
            (1 - (sum(correct_responses) / total_questions_in_lesson_set))
            / (sum(correct_responses) / total_questions_in_lesson_set)
        )
    except:
        if all(response == 0 for response in correct_responses):
            return 4
        else:
            return -4


# calculating correctness_prob
def calculate_correctness_prob(ability_parameter, lesson_difficulty):
    return ((math.e) ** (ability_parameter - lesson_difficulty)) / (
        1 + (math.e) ** (ability_parameter - lesson_difficulty)
    )


def update_user_proficiency(
    user_proficiency,
    lesson_difficulty,  # To be calculated
    correctness_probability,
    total_responses_of_question,# Us question ke kitne Response hai
    total_question_count, # Total Questions in a domain
):
    ability_parameter = calculate_ability_parameter(
        total_responses_of_question, 4, total_question_count
    )
    new_user_proficiency = (
        user_proficiency
        + (lesson_difficulty - ability_parameter) * correctness_probability
    )

    # range (0-1)
    new_user_proficiency = max(0, min(1, new_user_proficiency))

    return new_user_proficiency


def generate_questions(num_questions# Total Questions to be generated in next set
                       , question_difficulties# Difficulties of all Questions on specialization
                       , user_proficiency): 
    questions = []

    # Define a range around user proficiency for selecting questions
    range_threshold = 0.3  # for now

    for _ in range(num_questions):
        # Generating a random value within the range around user proficiency
        rand_value = random.uniform(
            user_proficiency - range_threshold, user_proficiency + range_threshold
        )

        # Finding the closest question difficulty to the random value within the range
        closest_difficulty = min(
            question_difficulties, key=lambda x: abs(x - rand_value)
        )

        # Determine if the user can answer the question based on the difference between user proficiency and question difficulty
        can_answer = user_proficiency >= closest_difficulty

        # Creating a tuple with question difficulty and a flag indicating if the user can answer it
        question = (closest_difficulty, can_answer)
        questions.append(question)

    return questions
