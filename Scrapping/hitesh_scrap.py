# step 0: Install all the requiremets

# pip Install requests
# pip Install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
# url="https://www.codewithharry.com/"
# url="https://programmingwithmosh.com/"
url="https://padhai.onefourthlabs.in/courses/data-science"
# step 1:- get the HTML
r=requests.get(url)
htmlContent = r.content
# print(htmlContent)
# step 2:- PARSE the HTML
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)
# step 3:- HTML tree traversal
# commonly used types of object

# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup 
# 4. Comment
title=soup.title #get the title of the url

# get all the para
paras=soup.find_all('p')

# anchor=soup.find_all('a')
# # get all the links from the page
# for link in anchor:
#     print(link.get('href'))

# Get classes of any elements in the HTML page
# print(soup.find('p')['class'])

# find all the elements with class lead
# print(soup.find_all("p", class_='lead'))

# Get teh text from the tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())

anchor=soup.find_all('a')
# get all the links from the page
# for link in anchor:
#     print(link.get('href'))
    
item=soup.find(id='main-content')
for elm in item.contents:
    print(elm)
