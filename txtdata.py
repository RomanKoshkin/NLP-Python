# retrieved from:
# https://www.sketchengine.co.uk/wp-content/uploads/test_python3.py

debug = True
root_url = 'https://the.sketchengine.co.uk'
base_url = '%s/bonito/run.cgi/' % root_url

# This does the logon and authentication. You'll need to do this first.
# Both of the options below need the requests.Session object, "s",
# which is set up below
# a test for demonstration using Sketch Engine through json interface
import requests
import urllib.parse
import json
import time


username = 'nightman'
password = '4hrs5UUSX6'
login_url = 'https://the.sketchengine.co.uk/login/'
logindata = {'username': username, 'password': password, 'submit': 'ok'}
method = 'view'
corp = 'preloaded/rutenten11_8' #  'bnc2'
# creating query string
attrs = dict(corpname=corp, q='', pagesize='1', format='json')
query_list = []
a = []


# def writefile(filename, data):
#     f = open(filename, 'w')
#     f.writelines(i + '\n' for i in data)
#     f.close()


def create_sess():
    s = requests.Session()
    s.auth = (username, password)
    s.get(login_url)
    r = s.post(login_url, data=logindata)

    # You want this to be NOT an empty list!!!
    print("Cookies:" + str(s.cookies.keys()))

    if debug == True:
        print("request headers:" + str(r.request.headers) + "\n")
        print("request text:" + str(r.request) + "\n")
        print("response headers:" + str(r.headers) + "\n")
        print("response code:" + str(r.status_code) + "\n")

    return s


# load, clean up, find unique, and sort the strings the strings
def load_once():
    i = []
    f_in = open('lemmasRus.txt', 'r')
    f_out = open('lemmasRus_unique.txt', 'w')
    for j in f_in.readlines():
        i.append(j.replace('\n', ''))
    i = set(i)
    i = list(i)
    i.sort()
    f_in.close()
        f_out.writelines(k + '\n' for k in i)
    f_out.close()
    return i


for j in load_once():
    #query_list.append('[word=\"' + j + '\"]')
    #query_list.append('[lemma=\"(?i)' + j + '\" & tag=\"(?i)V.*\"]')
    if j == '':
        continue
    else:
        query_list.append(u'[lemma=\"' + j + u'\"]')

count = 0
f = open('results.txt', 'a')    # appending new values
s = create_sess()
while count < len(query_list):
    try:
        query = query_list[count]
        print('about to  request: ' + str(count) + ' ' + query)
        attrs['q'] = 'q' + query
        encoded_attrs = urllib.parse.quote(json.dumps(attrs))
        url = base_url + method + '?json=%s' % encoded_attrs

        # this is the requests.Session object we created and set up earlier
        r = s.get(url)
        json_obj = r.json()
    except ValueError:
        print('LIMIT EXCEEDED. ABOUT TO RE-LOG IN')
        f.close()
        f = open('results.txt', 'a')    #'a' not to write but to append
        print('DATA BACKED UP. WAITING 20 SECONDS')
        time.sleep(20)  # take some time out
        s = create_sess()
    else:
        a.append(json_obj.get(u'concsize', u'0'))
        print(query + '\t' + str(json_obj.get(u'concsize', u'0')))
        f.write(str(count) + '\t' + query_list[count] + '\t' + str(a[count]) + '\n')
        count += 1

f.close()
print('end of job')

# b = []
# for i in a:
#     i = str(i)
#     b.append(i.replace('\n', '')) # get rid of line breaks
#
# b = set(b)      # get unique entries
# b = list(b)     # convert back to a list
# writefile('RusUniqueSorted.txt', b)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! [lemma="(?i)tests" & tag="(?i)V.*" ]

# a = pd.read_excel('wrds.xlsx', header=None, skiprows=1)
# query_list[i] + '\t' + str(a[i]) + '\n' for i in range(len(a)))


# # demonstration NOT using the json input interface
# import json
# import urllib.parse
#
# corp = 'bnc2'
# method = 'view'
# attrs = dict(corpname=corp, q='', pagesize='200', format='json')
# query_list = ['[lemma="test"]', '[lemma="drug"][lemma="test"]', '[lemma="blood"][lemma="test"]',
#               '[lemma="test"][lemma="result"]']
#
# for query in query_list:
#     attrs['q'] = 'q' + query
#     encoded_attrs = urllib.parse.urlencode(attrs)
#     url = base_url + method
#     # The "s" in the line below is the requests.Session object we
#     # created and set up earlier
#     # The requests module can handle building the url parameter stuff
#     # We just give it a dictionary (attrs)
#     r = s.get(url, params=attrs)
#     if debug == True:
#         print(r.request.url)
#         print(urllib.parse.unquote(r.request.url))
#         print(r.status_code)
#         print(r.headers)
#     # json data stuff
#     # the requests module also handles the json output nicely. ;)
#     json_obj = r.json()
#     print(query + '\t' + str(json_obj.get('concsize', '0')))
#
# # prints the fifth concordance line / entry
# print(json.dumps(json_obj["Lines"][5], sort_keys=True, indent=4))