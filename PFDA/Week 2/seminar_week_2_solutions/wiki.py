# -*- coding: utf-8 -*-
"""
Created on Tue Jan  17 13:15:47 2022

@author: zzw
"""


import requests
import json
import csv

# 1 using full url
url = "https://en.wikipedia.org/w/api.php?action=query&format=json\
&prop=revisions&titles={}&formatversion=2&rvprop=timestamp|user|comment&rvlimit=5"
titles = [
    'University of Warwick',
    'Coventry University',
    'University of Birmingham'
]

for title in titles:
    result = requests.get(url.format(title))
#    print(result.text)
    result_dict = json.loads(result.text)
#    print(result_dict['query']['pages'][0]['revisions'][0])
    revisions = result_dict['query']['pages'][0]['revisions']
    for revision in revisions:
        record = [title]
        for value in revision.values():
            record.append(value)
        with open('wiki1.csv', 'a', newline="") as savefile:
            writecsv = csv.writer(savefile)
            writecsv.writerow(record)


# 2 using payload
url = "https://en.wikipedia.org/w/api.php"
titles = [
    'University of Warwick',
    'Coventry University',
    'University of Birmingham'
]
payload = {
    'action': 'query',
    'format': 'json',
    'prop': 'revisions',
    'formatversion': 2,
    'rvprop': 'timestamp|user|comment',
    'rvlimit': 5
}
for title in titles:
    #    result = requests.get(url.format(title))
    payload['titles'] = title
    result = requests.get(url, params=payload)
#    print(result.text)
    result_dict = json.loads(result.text)
#    print(result_dict['query']['pages'][0]['revisions'][0])
    revisions = result_dict['query']['pages'][0]['revisions']
    for revision in revisions:
        record = [title]
        for value in revision.values():
            record.append(value)
        with open('wiki2.csv', 'a', newline="") as savefile:
            writecsv = csv.writer(savefile)
            writecsv.writerow(record)
