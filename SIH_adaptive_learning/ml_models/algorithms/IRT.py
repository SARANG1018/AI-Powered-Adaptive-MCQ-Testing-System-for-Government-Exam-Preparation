# Item Response Theory
import math             
ability_of_student=0.4
difficulty_of_question=0.5

def logit(p):
    try:
        return math.log(p/(1-p))
    except:
        return p

def logit_inverse(x):
    return 1/(1+math.exp(-x))

# 1PL IRT Model
def IRT_1PL_Probab(ability_of_student,difficulty_of_question):
    return 1/(1+math.exp(-1*(ability_of_student-difficulty_of_question)))

def next_ability_onIRT_1PL(ability_of_student,difficulty_of_question):
    probability=IRT_1PL_Probab(ability_of_student,difficulty_of_question)
    temp=logit(probability) #logit
    return logit_inverse(temp+difficulty_of_question)

def next_difficulty_onIRT_1PL(ability_of_student,difficulty_of_question):
    probability=IRT_1PL_Probab(ability_of_student,difficulty_of_question)
    temp=logit(probability) #logit
    return logit_inverse(ability_of_student-temp)

def calculate_discrimination_param(ability_of_student,difficulty_of_question):
    print("Discrim param :")
    print(ability_of_student)
    print(difficulty_of_question)
    return logit(IRT_1PL_Probab(ability_of_student,difficulty_of_question))-logit(IRT_1PL_Probab(ability_of_student,difficulty_of_question))

# 3PL_IRT Model 
def IRT_3PL_Probab(ability_of_student,difficulty_of_question,chance_of_guessing=0.25):
    discrimination_param=calculate_discrimination_param(ability_of_student,difficulty_of_question)
    return chance_of_guessing+(1-chance_of_guessing)*logit(discrimination_param*(ability_of_student-difficulty_of_question))

def next_ability_onIRT_3PL(ability_of_student,difficulty_of_question,chance_of_guessing=0.25):
    probability=IRT_3PL_Probab(ability_of_student,difficulty_of_question,chance_of_guessing)
    temp=logit(probability) #logit
    return logit_inverse(difficulty_of_question+temp)

def next_difficulty_onIRT_3PL(ability_of_student,difficulty_of_question):
    probability=IRT_3PL_Probab(ability_of_student,difficulty_of_question)
    temp=logit(probability) #logit
    return logit_inverse(ability_of_student-temp)

# Performance Function Algorithm
# def PFA(ability_of_student,difficulty_of_question,observed_indicators, interaction_parameters):
#     baseline_term=ability_of_student
#     difficulty_sum=sum(difficulty_of_question)
#     interaction_term = sum((beta + y * c) for beta, y, c in zip(difficulty_of_question, observed_indicators, interaction_parameters))
#     return baseline_term + difficulty_sum + interaction_term





