from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj = bs(html, 'html.parser')

#nameList = bsObj.find_all('span',{'class':'green'})
nameList = bsObj.find_all({'h1','h2'}) #retorna lista das tags procuradas
#nameList = bsObj.find_all('span', {'class':'green', 'class':'red'}) #retona tags de span green e red
#nameList = bsObj.find_all(text='the prince') print(len(nameList)) #retona o número de ocorrência da palavra
allText = bsObj.find_all(id='text') #retorna o conteúdo do id text
print(allText)

for name in nameList:
    print(name)

#print(bsObj)