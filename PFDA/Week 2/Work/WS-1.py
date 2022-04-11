#Jedlueng 21 January 2021 
#Extract required information 
#(https://www.wbs.ac.uk/about/person/zhewei-zhang):
#Email, phne number, room number, modules taught

from contextlib import ContextDecorator
import email
import requests 
from bs4 import BeautifulSoup

#Request the webpage 
url = 'https://www.wbs.ac.uk/about/person/zhewei-zhang'


html = requests.get(url)

#Get text
content = html.text

# parse html content(restructure)
soup = BeautifulSoup(content, 'html.parser')

# Finding by class name
# #Email
# email = str(soup.find(class_ = "email" ))
# #Slice string
# email = email[30:52]


#Find contact info
email = soup.find(class_ = "contactinfo").find_all('a')[0].text
room = soup.find(class_ = "contactinfo").find_all('a')[2].text


print('This is email {} , this is room {}'.format(email,room))
#Module taught 




#String