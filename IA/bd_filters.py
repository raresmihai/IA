from bd_aiml import respond_from_aiml
from math_module import get_math_response
from scraping import get_answer

def get_yes_or_no_response(input):
    # TO DO
    return ''


def get_personal_question_response(input):
    # TO DO
    return respond_from_aiml(input)


def get_choose_between_response(input):
    # TO DO
    return ''


def get_difference_between_response(input):
    # TO DO
    return ''


def get_info_about_response(input):
    # TO DO
    return ''


def get_math_question_response(input):
    # TO DO
    #Pe ultima pozitie am nevoie sa fie fraza intreaga introduse sa utilizator
    return get_math_response(input[len(input) - 1])


def get_doubts_response(input):
    # TO DO
    return respond_from_aiml(input)
