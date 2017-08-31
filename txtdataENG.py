import requests
import urllib.parse
import json
import time


class Qwer(object):

    def __init__(self): # эта ф-ция автоматически срабатывает, когда мы инициализируем объект x = Qwer()
                        # SELF - ЭТО как бы заменитель названия инстанса класса. Это контейнер, где будут храниться
                        # все переменные инстанса класса, к которым можно обращаться извне и изнутри
                        # SELF - это как бы глобальный для инстанса класса контейнер с переменными (объектами)
        ############################################################# parameters:
        debug = True
        username = 'nightman'
        password = '4hrs5UUSX6'
        login_url = 'https://the.sketchengine.co.uk/login/'
        logindata = {'username': username, 'password': password, 'submit': 'ok'}
        #############################################################################

        self.s = requests.Session()
        self.s.auth = (username, password)
        self.s.get(login_url)
        self.r = self.s.post(login_url, data=logindata)

        # You want this to be NOT an empty list!!!
        print("Cookies:" + str(self.s.cookies.keys()))

        if debug == True:
            print("request headers:" + str(self.r.request.headers) + "\n")
            print("request text:" + str(self.r.request) + "\n")
            print("response headers:" + str(self.r.headers) + "\n")
            print("response code:" + str(self.r.status_code) + "\n")

    def RequestFreq(self, *arg):
        method = 'view'
        corp = 'bnc2'  # rutenten11_8'
        root_url = 'https://the.sketchengine.co.uk'
        base_url = '%s/bonito/run.cgi/' % root_url
        attrs = dict(async='0', corpname=corp, q='', pagesize=1000000, format='json')
        query = '[lemma=\"(?i)' + str(arg[0]) + '\"]' # arg[0] because arg is a tuple
        # if not "s" in dir():
        #     s = self.create_sess()
        try:
            print('about to  request: ' + query)
            attrs['q'] = 'q' + query
            encoded_attrs = urllib.parse.quote(json.dumps(attrs))
            url = base_url + method + '?json=%s' % encoded_attrs

            # this is the requests.Session object we created and set up earlier
            self.r = self.s.get(url)
            json_obj = self.r.json()
        except ValueError:
            print('LIMIT EXCEEDED. ABOUT TO RE-LOG IN')
            time.sleep(20)  # take some time out
            self.s = self.__init__()
        else:
            return json_obj.get(u'concsize', u'0')
