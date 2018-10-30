from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = bs(html, 'html.parser')

#children
for child in bsObj.find('table',{'id':'giftList'}).children:
    print(child)

#descendants
#for child in bsObj.find('table',{'id':'giftList'}).descendants:
#    print(child)

#siblings
#for sibling in bsObj.find('table',{'id':'giftList'}).tr.next_siblings: #.previous_sibling
#    print(sibling)

#parents
#print(bsObj.find('img',{'src':'../img/gifts/img2.jpg'}).parent.previous_sibling.get_text())