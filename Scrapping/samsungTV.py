from re import sub
from decimal import Decimal
import requests
from bs4 import BeautifulSoup
url='https://www.flipkart.com/samsung-80cm-32-inch-hd-ready-led-tv/p/itm0d0c1abe665c0?pid=TVSFZRNNEEEXPGGG&lid=LSTTVSFZRNNEEEXPGGGNUF3GW&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_158e58ae-2b74-4a1d-854e-2323401ef216_10_LN5W971UVDSD_MC.TVSFZRNNEEEXPGGG&ppt=clp&ppn=television-store&ssid=vx2vbsv2f40000001591614857248&otracker=clp_pmu_v2_Mi%252C%2BVu%252C%2BSamsung%2B%2526%2Bmore_6_10.productCard.PMU_V2_Mi%252C%2BVu%252C%2BSamsung%2B%2526%2Bmore_television-store_TVSFZRNNEEEXPGGG_neo%2Fmerchandising_5&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Mi%252C%2BVu%252C%2BSamsung%2B%2526%2Bmore_LIST_productCard_cc_6_NA_view-all&cid=TVSFZRNNEEEXPGGG'
# step 1: Get the HTML 
r=requests.get(url)
content=r.content
# step 2: Parse the content
content=r.content
soup=BeautifulSoup(content,"html.parser")
# step 3: HTML traversal
element=soup.find('div',{'class':'_1vC4OE _3qQ9m1'})
price=element.text.strip()[1:]
# print(price)
value=Decimal(sub(r'[^\d.]','',price))
# print(type(value))
if value >= 12000:
    print("Buy the TV with price value {}".format(price))
else:
    print('Dont buy the tv')
