"""this makes a request to the website, receives a reply, parses it and gets the data you want"""


import requests
from bs4 import BeautifulSoup

wrd = []
lemmas = []

f_in = open('Rus.txt', 'r')
for j in f_in.readlines():
    wrd.append(j.replace('\n', ''))

count = 367
for token in wrd[count:]:

    a = ''
    link = "https://www.lingvolive.com/en-us/translate/ru-en/" + token + '\"'
    html = requests.get(link).text
    """If you do not want to use requests then you can use the following code below
       with urllib (the snippet above). It should not cause any issue."""
    soup = BeautifulSoup(html)
    heading = soup.h1
    try:
        _ = (e for e in heading)
    except TypeError:
        print('object is not iterable')
    else:
        for i in heading:
            a += ''.join(i.contents)
        lemmas.append(a)
        count += 1
        print(count)
        f = open('lemmasfromAbbyy.txt', 'a')
        f.write(str(count) + '\t' + token + '\t' + a + '\n')
        f.close()