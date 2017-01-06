from bs4 import BeautifulSoup
import requests
import dryscrape
import time
import re

# web_page_template = "https://www.google.com/search?q={query_string}&oq={query_string}&aqs=chrome..69i57.6342j0j4&sourceid=chrome&ie=UTF-8"
web_page_template = "https://www.google.ro/webhp?hl=en&sa=X&ved=0ahUKEwiN1fnSh67RAhUGDiwKHcd8AQwQPAgD#hl=en&q={query_string}"
search_content = [["span", "class", "_m3b"], ["span", "class", "_XWk"],
                  ["span", "class", "wob_t"], ["span", "class", "_Ex"]]
session = dryscrape.Session()


def search(soup):
    for item in search_content:
        try:
            answer = soup.findAll(item[0], {item[1]: item[2]})[0].content[0]
            return answer
        except Exception as e:
            print e
    try:
        answer = soup.select('div[class="_tXc"] > span')[0].contents[0]
        return answer
    except Exception as e:
        print e

    try:
        answers = soup.findAll("span", {"class": "st"})
        best_answer = ""
        max_occurrence = 0
        regex = re.compile('<b>.*?</b>')
        regex_remove_html_tags = re.compile("<.*?>")
        for answer in answers:
            message = ""
            for content in answer.contents:
                message += content.encode("UTF-8")
            key_work_occurrence = regex.findall(message)
            occurrence = get_number_of_key_word_apperence(key_work_occurrence, regex)
            if occurrence > max_occurrence:
                max_occurrence = occurrence
                best_answer = regex_remove_html_tags.sub("", message)

        print "Best_Answer=", best_answer
        return best_answer
    except Exception as e:
        print e
    return ""


def get_number_of_key_word_apperence(occurrence, regex):
    return max([len(x.split(" ")) for x in occurrence])


def get_answer_from_page(web_page):
    aux = time.time()
    response = requests.get(web_page)
    soup = BeautifulSoup(response.text.encode("UTF-8"), "html.parser")
    content = soup.prettify(encoding="UTF-8")
    # file_object = open("response.html", mode="wt")
    # file_object.write(content)
    # file_object.close()
    answer = search(soup)
    print time.time() - aux
    return answer


def get_answer_from_rendered_page(web_page):
    start_time = time.time()
    session.visit(web_page)
    response = session.body()
    soup = BeautifulSoup(response, "html.parser")
    content = soup.prettify(encoding="UTF-8")
    # file_object = open("response_r.html", mode="wt")
    # file_object.write(content)
    # file_object.close()

    answer = search(soup)
    print time.time() - start_time
    return answer


def get_answer(search_string):
    web_page = web_page_template.format(query_string=search_string)
    print web_page
    answer = get_answer_from_page(web_page)
    if answer == "":
        print "Failed to get an answer without rendering the page"
        answer = get_answer_from_rendered_page(web_page)
    return answer


if __name__ == "__main__":
    answer = get_answer("km+between+Iasi+and+Suceava")
    print "Answer=", answer
