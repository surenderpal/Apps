import requests
from bs4 import BeautifulSoup
# request=requests.get("https://www.johnlewis.com/2020-apple-macbook-pro-13-inch-touch-bar-intel-core-i5-8gb-ram-256gb-ssd/p5015351")
request=requests.get("https://www.amazon.com/Electric-Rotary-Trimmer-Display-Waterproof/dp/B07WVSS16Q?ref_=Oct_DLandingS_D_22046e21_60&smid=AFUJM8UR8X25D")
# request=requests.get("https://www.alibaba.com/product-detail/Strong-Bass-Rename-GPS-Apple-AirPods_62347389859.html?spm=a27aq.13274681.9336958460.63.59a93456frQwCL")

# price price--large
# <p class="price price--large">£1,299.00</p>

content=request.content
soup=BeautifulSoup(content,"html.parser")
# print(soup.prettify())
# element=soup.find("p",{"class":"price price--large"})
# <span class="ma-reference-price-highlight" data-spm-anchor-id="a2700.wholesale.maonnacta.i0.41951c0bl4VhNN">US$&nbsp;15.00 - US$&nbsp;39.90</span>
# <span id="priceblock_dealprice" class="a-size-medium a-color-price priceBlockDealPriceString">$35.27</span>

# element=soup.find("span",{"class":"a-size-medium a-color-price priceBlockDealPriceString"})
element=soup.find("span",{"id":"priceblock_dealprice"})
print(element.text.strip())
