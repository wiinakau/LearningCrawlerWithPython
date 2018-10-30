from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as err:
        print(err)
        return None

    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        title = bsObj.body.h1
    except AttributeError as err:
        return None
    return title

title = getTitle('http://pythonscraping.com/exercises/exercise1.html')

if title == None:
    print('Titulo não encontrado')
else:
    print(title)