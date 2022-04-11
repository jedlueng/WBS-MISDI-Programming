# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 13:43:53 2022

@author: zzw
"""
import csv
import requests
from bs4 import BeautifulSoup
url = "https://www.wbs.ac.uk/about/person/zhewei-zhang"
result = requests.get(url)
url_content = BeautifulSoup(result.text, 'html.parser')
contact = url_content.find(class_='contactinfo').find_all('a')
email = contact[0].text.strip()
phone = contact[1].text.strip()
room = contact[2].text.strip()

teaching = url_content.find(class_='teaching').find_all('li')
modules = []
for module in teaching:
    modules.append(module.text.strip())

print(email, phone, room, modules)

###########################################
url = "https://www.wbs.ac.uk/research/staff/"
result = requests.get(url)
url_content = BeautifulSoup(result.text, 'html.parser')
profiles = url_content.find_all(class_='person-thumbnail')

with open('profile.csv', 'a', newline="", encoding='utf-8') as wf:
    wbs_writer = csv.writer(wf)
    for profile in profiles:
        info = []
        # .get() will return the value of the specified attribute
        info.append(profile.get('data-fullname')) 
        info.append(profile.get('href'))
        info.append(profile.get('data-jobtitle'))
        wbs_writer.writerow(info)
