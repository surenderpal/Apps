import requests
from bs4 import BeautifulSoup
url=requests.get("https://www.amazon.com/Electric-Rotary-Trimmer-Display-Waterproof/dp/B07WVSS16Q?ref_=Oct_DLandingS_D_22046e21_60&smid=AFUJM8UR8X25D")
content=url.content
soup=BeautifulSoup(content,"html.parser")
element=soup.find("span",{"id":"priceblock_dealprice"})
print(element.text.strip())