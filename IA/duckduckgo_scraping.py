import duckduckgo
import json
from bs4 import BeautifulSoup
import requests
import dryscrape

duckduckdo_query_page = "https://duckduckgo.com/?q={info}"
session = dryscrape.Session()


def query_web_page_duckduckgo(web_page):
    print(web_page)
    response = session.body()
    soup = BeautifulSoup(response, "html.parser")
    content = soup.prettify(encoding="UTF-8")
    # file_object = open("response_duck.html", mode="wt")
    # file_object.write(content)
    # file_object.close()
    return soup.find("div", {"class": "module__text"})


def get_answer(search_string):
    try:
        search_result = duckduckgo.query(search_string)
        # file_object = open("result.json", "wt")
        # json.dump(search_result.json, file_object)
        # file_object.close()
    except Exception as e:
        print e
        return ""

    answer = search_result.abstract.text
    if answer == "":
        print "Instant answer failed"
        answer = query_web_page_duckduckgo(duckduckdo_query_page.format(info=search_string.replace(" ", "+")))
        if answer is None:
            print "Web scrap failed"
            answer = ""
        return answer
    else:
        print "Instant API success response"
        return answer


if __name__ == "__main__":
    get_answer("Abraham Lincoln")
