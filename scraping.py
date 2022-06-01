from bs4 import BeautifulSoup
import requests

API = "https://www.linkcorreios.com.br/?id="
def findByCode(code):
    source = requests.get(API + code).text
    soup = BeautifulSoup(source, 'html.parser')
    mainData = soup.find('div', class_='card-header')
    lastStatus = mainData.find('h2').text
    listItems = mainData.find_all('li')
    items = [lastStatus]
    for li in listItems:
        items.append(li.get_text())
    historicoUl = soup.find_all('ul', class_='linha_status')
    historicoDicionario = []
    for index, li in enumerate(historicoUl):
        historicoDicionario.append(li.get_text()[1:].split('\n'))
    return (items,historicoDicionario)