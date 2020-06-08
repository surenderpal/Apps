import requests
from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal
url='https://www.flipkart.com/apple-iphone-11-white-64-gb/p/itm2644c3764fc54?pid=MOBFKCTSHAWGGFHM&lid=LSTMOBFKCTSHAWGGFHMCPQSMX&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_3_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_3_7_na_na_na&fm=SEARCH&iid=a0f8d8e6-2a6c-4263-a2e8-f18200b05241.MOBFKCTSHAWGGFHM.SEARCH&ppt=sp&ppn=sp&ssid=rpii61ioj40000001591617619694&qH=f6cdfdaa9f3c23f3'
# step 1: Get the HTML  
r=requests.get(url)
# step 2: Parse the content
content=r.content
soup=BeautifulSoup(content,'html.parser')
# step 3: HTML traversal
element = soup.find('div',{'class':'_1vC4OE _3qQ9m1'})
amount=element.text.strip()[1:]
desc=soup.find('span',{'class':'_35KyD6'})
print(desc.text)
print(element.text)
BankOffer=soup.findAll('div',{'class':'_3D89xM'})
for span in BankOffer:
    span=span.find_next('span').find_next('span').find_next('span')
    print(span.text)