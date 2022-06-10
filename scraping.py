# @file scraping.py
# Imports
from bs4 import BeautifulSoup
import requests

API = "https://www.linkcorreios.com.br/?id="
def findByCode(code):
    """
    Função responsável por realizar a busca das informações no link fornecido pelo arquivo constants.py
    e mostrar na tela a table com as informações adquiridas
    :param code: String contendo o código de rastreio informado pelo usuário
    :return:
    """
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