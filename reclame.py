from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep

baseURL = 'https://www.reclameaqui.com.br'
empresa = '/indices/lista_reclamacoes/?id=902&status=ALL'

driver = webdriver.Firefox()
driver.get(f'{baseURL}{empresa}')
sleep(3)

bsObj = bs(driver.page_source, 'html.parser')

itens = bsObj.find_all('div', {'class':'complain-status-title'})
href_links = [item.find('a').get('href') for item in itens]
page_links = [f'{baseURL}{link}' for link in href_links]
#print(href_links)

for link in page_links:
    driver.get(link)
    sleep(2)
    bsPage = bs(driver.page_source, 'html.parser')
    titulo = bsPage.find('h1', {'class':'ng-binding'}).text
    reclamacao = bsPage.find('div', {'class':'complain-body'}).text

    print(
        'Titulo: {}\n\n'.format(titulo),
        'Reclamação: {}\n\n'.format(reclamacao)
    )