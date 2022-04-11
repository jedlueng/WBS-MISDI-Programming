#Jedlueng 21 January 2021 
#Find all the staff name of  https://www.wbs.ac.uk/research/staff/?department=IKON


import requests 
from bs4 import BeautifulSoup

#Request the webpage 
url = 'https://www.wbs.ac.uk/research/staff/?department=IKON'

html = requests.get(url)

print(html.status_code)

#Get text
content = html.text

# parse html content
soup = BeautifulSoup(content, 'html.parser')


name = soup.findAll(class_ = 'person')

