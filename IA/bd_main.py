from random import randint
from random import choice
from bd_conversation_changers import conversation_changers
from bd_conversation_changers import personal_questions
from bd_filters import get_yes_or_no_response
from bd_filters import get_personal_question_response
from bd_filters import get_choose_between_response
from bd_filters import get_difference_between_response
from bd_filters import get_info_about_response
from bd_filters import get_math_question_response
from bd_filters import get_doubts_response
from bd_aiml import initialize_aiml_module

class BD:
    def __init__(self):
        self.count = 0
        self.conversation_changers = conversation_changers
        self.personal_questions = personal_questions
        initialize_aiml_module()

    #input = (filter, is_question_flag, synonyms, keywords, input_phrase)
    def get_response(self,input):
        self.count += 1
        is_question = input[1]

        if is_question:
            return self.find_response_by_filter(input)
        else:
            #if there were at least 3 inputs from the user,
            #there is a 15% chance to change the conversation
            epsilon = randint(0,99)
            if epsilon < 15 and self.count > 3:
                return self.change_conversation(input)
            else:
                return self.find_response_by_filter(input)


    def find_response_by_filter(self, input):
        try:
            filters = ["YesOrNo","PersonalQuestion","ChooseBetween",
                       "DifferenceBetween", "InfoAbout","MathQuestion","Doubts"]
            filter_value = input[0]
            if filter_value < 0:
                filter = "Doubts"
            else:
                filter = filters[filter_value]

            if filter is "YesOrNo":
                return get_yes_or_no_response(input)
            elif filter is "PersonalQuestion":
                return get_personal_question_response(input)
            elif filter is "ChooseBetween":
                return get_choose_between_response(input)
            elif filter is "DifferenceBetween":
                return get_difference_between_response(input)
            elif filter is "InfoAbout":
                return get_info_about_response(input)
            elif filter is "MathQuestion":
                return get_math_question_response(input)
            elif filter is "Doubts":
                return get_doubts_response(input)
            else:
                #should never reach this branch
                return get_doubts_response(input)
        except Exception as e:
            #should never reach this branch
            print e
            return get_doubts_response(input)

    # Change the conversation subject by using a conversation conversation changer
    # and then a personal queston
    # Example: I would like to know more about you. What's your occupation?
    def change_conversation(self,input):
        conversation_changer = self.get_conversation_changer()
        personal_question = self.get_and_remove_personal_question()
        if personal_question is not -1:
            return conversation_changer + personal_question
        else:
            return get_doubts_response(input)

    def get_conversation_changer(self):
        return choice(self.conversation_changers)

    #gets and removes the personal question so it doesn't repeat later
    def get_and_remove_personal_question(self):
        personal_q_count = len(self.personal_questions) - 1
        if personal_q_count >= 0:
            random_question = randint(0,personal_q_count)
            personal_question = self.personal_questions[random_question]
            del self.personal_questions[random_question]
            return personal_question
        return -1
