import duckduckgo_scraping
import google_scraping

"""
        list keyWords (cuvinte cheie si sinonime);
        O lista de tuple cu criterii si sinonime dupa caz;
        Exemplu:
        [(criteriu1,sinonim1),(criteriu2,sinonim2)]
        O lista cu subiecti;
"""


def get_answer_from_duck(key_words, question):
    """
        Function that retrieves an answer from duck
    :param key_words: Key words of the question
    :param question:  The question that was asked by user
    :return: An answer
    """

    aux = key_words[0]
    subjects = key_words[1]
    subjects_query = ""
    for subject in subjects:
        subjects_query += subject + " "
    subjects_query = subjects_query.strip()
    answer = duckduckgo_scraping.get_answer(subjects_query)
    if answer == "":
        # I search only using the subjects
        # I will try to search again using this time subject + one key_word
        print aux
        for item in aux:
            query_string = subjects_query + " " + item[0]
            answer = duckduckgo_scraping.get_answer(query_string)
            if answer != "":
                return answer

    return answer


def get_answer_from_google(key_words, question):
    """
            Function that retrieves an answer from duck
        :param key_words: Key words of the question
        :param question:  The question that was asked by user
        :return: An answer
    """

    aux = key_words[0]
    subjects = key_words[1]
    subjects_query = ""
    for subject in subjects:
        subjects_query += subject + " "
    subjects_query = subjects_query.strip()
    answer = google_scraping.get_answer(subjects_query)
    if answer == "":
        # I search only using the subjects
        # I will try to search again using this time subject + one key_word
        print aux
        for item in aux:
            query_string = subjects_query + " " + item[0]
            answer = google_scraping.get_answer(query_string)
            if answer != "":
                return answer

    return answer


def get_answer(input):
    """
        Function that returns a response from web scrapping
    :param input: Input received from text processing
    :return: An response
    """

    answer = get_answer_from_duck([[('is', ""), ("who", "")], ['Abraham', 'Lincoln']], 'Who is Abraham Lincoln?')
    if answer == "":
        print "Failed to receive an answer from duck"
        answer = get_answer_from_google([[('is', ""), ("who", "")], ['Abraham', 'Lincoln']], 'Who is Abraham Lincoln?')
        if answer == "":
            print "Failed to receive an answer from google"

    return answer


if __name__ == "__main__":
    print("Raspuns=", get_answer(""))
