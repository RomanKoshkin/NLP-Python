#!/usr/bin/env python
#coding=utf-8

import urllib.request as urllib2  # this is a neat trick to import urllib2 under python3
import simplejson

data = simplejson.dumps({
    'text': '''Some long text here...''',
    'language': 'english',
    'passphrase': '...passphrase...',
    'simple_maths_n': 10,
    'attribute': 'word',
    'exclude_stop_words': True,
    'alphanumeric': True,
    'one_alphabetic': True,
    'min_length': 3,
    'max_keywords': 10,
    'min_frequency': 5
    })

req = urllib2.Request("https://beta.sketchengine.co.uk/get_keywords/", data)
opener = urllib2.build_opener()
f = opener.open(req)
obj = simplejson.load(f)
if obj.get('error') == '':
    print('Length:', obj.get('length', 0))
    print('Reference corpus:', obj.get('ref_corp', ''))
    for k in obj.get('keywords', []):
        print('%s\t%d\t%f' % tuple(k))
else:
    print('Error encountered:', obj.get('error'))