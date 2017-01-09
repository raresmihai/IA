import string
import urllib
from collections import Counter
import operator

import duckduckgo
from google import google
from bs4 import BeautifulSoup


def get_best_phrase(text, key_words):
    try:
        if text == '':
            return ''
        # list of thrases
        phrases1 = []
        # string for storing a phrase ,appended to phrases1 and reused for next phrase
        phrase1 = ''
        # list stores phrases,a phrase as a list of words
        phrases2 = []
        # list of dictionaries. for each phrase create a dictionary of words
        dict1 = []
        # list of number of occurences of keywords in phrase
        dict2 = []
        for i in text:
            if i in '.' or i in '!' or i in ';' or i in '|':
                phrases1.append(phrase1)
                phrase1 = ''
            else:
                phrase1 += i

        for i in range(len(phrases1)):
            if phrases1[i] != '':
                if not 65 <= ord(phrases1[i][0]) <= 90:
                    phrases1[i] = ''
                for j in phrases1[i]:
                    if j in '?':
                        phrases1[i] = ''
                nums = [int(s) for s in phrases1[i].split() if s.isdigit()];
                if len(nums) > 1:
                    phrases1[i] = ''

        for i in phrases1:
            if i != '':
                temp = []
                phrase2 = i.split()
                # print phrase2
                for j in phrase2:
                    temp.append(j)
                phrases2.append(temp)

        for i in range(len(phrases2)):
            for j in phrases2[i]:
                if j.isupper():
                    if len(j) > 4:
                        phrases2[i] = []

        for i in range(len(phrases2)):
            dict1.append(dict(Counter(phrases2[i])))
        # max occurences
        for i in range(len(dict1)):
            for key, value in dict1[i].iteritems():
                if value > 1:
                    dict1[i].clear()
                    phrases2[i] = []
                    break

        maxx = 0
        for i in dict1:
            for j in key_words:
                if j in i:
                    maxx += 1
            dict2.append(maxx)
            maxx = 0

        if not dict2:
            return ''
        index, value = max(enumerate(dict2), key=operator.itemgetter(1))
    except:
        print 'except'
        return ''
    return str(' '.join(phrases2[index]).encode('utf-8').strip())


def get_text_from_html_page(url):
    try:
        if url == '':
            return ''
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()  # rip it out

        # get text
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        # return text
    except:
        return ''
    return text


def duckduckgo_result(search_string):
    try:
        search_results = duckduckgo.query(search_string)

        print search_results.abstract.url
        url = ''
        for i in search_results.abstract.url:
            if i in '(':
                break
            else:
                url += i
    except:
        return ''
    return url


def google_results(search_string):
    try:
        search_results = google.search(search_string, 1)
        print search_results[0].link
    except:
        return []
    return search_results


def return_search_on_google(search_type, input_type, words_synonyms, key_words, text):
    try:
        answer = ''
        search_string = ''
        all_words = []
        for i, j in words_synonyms:
            search_string += '"' + i + '" OR ' + '"' + j + '" '
            all_words.append(i)
            all_words.append(j)
        for i in key_words:
            search_string += ' "' + i + '"'
            all_words.append(i)

        print 'search string ='
        search_string += ' english'
        print search_string
        temp = all_words[:]

        search_results_google = google_results(text)
        if not search_results_google:
            search_results_google = google_results(search_string)
        if search_results_google:
            answer += get_best_phrase(get_text_from_html_page(search_results_google[0].link), all_words)
        if answer == '':
            temp.insert(0, 'dummy data')
            while answer == '' and temp:
                del temp[0]
                str = ' '.join(temp)
                print str
                answer += get_best_phrase(
                    get_text_from_html_page(duckduckgo_result(str)),
                    all_words)
        print 'anwser='
        print answer
        return answer
    except:
        return ''


return_search_on_google(0, True, [('', 'meaning')], ['life'], 'what is the meaning of life?')
