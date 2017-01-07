from bd_aiml import respond_from_aiml
from math_module import get_math_response
from scraping import get_response_from_web


def get_yes_or_no_response(input):
    # TO DO
    return ''


def get_personal_question_response(input):
    # TO DO
    return respond_from_aiml(input)


def get_choose_between_response(input):
    # TO DO
    answer = get_response_from_web(input)
    if answer == "":
        answer = respond_from_aiml(input)
    return answer


def get_difference_between_response(input):
    # TO DO
    answer = respond_from_aiml(input)
    if answer == "":
        answer = get_response_from_web(input)
    return answer


def get_info_about_response(input):
    # TO DO
    return ''


def get_math_question_response(input):
    # TO DO
    # Pe ultima pozitie am nevoie sa fie fraza intreaga introdusa de utilizator
    return get_math_response(input[len(input) - 1])


def get_doubts_response(input):
    # TO DO
    return respond_from_aiml(input)
