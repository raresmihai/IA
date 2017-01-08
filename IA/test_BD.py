from unittest import TestCase

from bd_main import BD


class TestBD(TestCase):

    bd = BD()

    def test_get_response_for_yes_or_no_filter(self):
        bd = self.bd
        input_tuple = (0, True, [('', '')], ['', ''],
                       'Do you like to read books?')
        print 'Yes or no filter answer: ' + bd.get_response(input_tuple)

    def test_get_response_for_personal_question_filter(self):
        bd = self.bd
        input_tuple = (1, True, [('', '')], ['', ''],
                       'What do you like to do?')
        print 'Personal question filter answer: ' + bd.get_response(input_tuple)

    def test_get_response_for_choose_between_filter(self):
        bd = self.bd
        input_tuple = (2, True, [('', '')], ['equator', 'north pole'],
                       'What do you like the most, equator or north pole?')
        print 'Choose between filter answer: ' + bd.get_response(input_tuple)

    def test_get_response_for_difference_between_filter(self):
        bd = self.bd
        input_tuple = (3, True, [('', '')], ['equator', 'north pole'],
                       'What do you like the most, equator or north pole?')
        print 'Difference between filter answer: ' + bd.get_response(input_tuple)

    def test_get_response_for_info_about_filter(self):
        bd = self.bd
        input_tuple = (4, True, [('', '')],
                   ['meaning', 'life'],
                   'What is the meaning of life?')
        print 'Info about filter answer: ' + bd.get_response(input_tuple)

    def test_get_response_for_math_filter(self):
        bd = self.bd
        input_tuple = (5, True, [('', '')], [''], '')
        print 'Math filter answer: ' + bd.get_response(input_tuple)

    def test_get_response_for_doubts_filter(self):
        bd = self.bd
        input_tuple = (6, True, [('', '')], [''], 'How is weather today?')
        print 'Doubts filter answer: ' + bd.get_response(input_tuple)
