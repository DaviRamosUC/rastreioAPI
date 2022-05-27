from bs4 import BeautifulSoup
from constants import API
import requests


def findByCode(code):
    source = requests.get(API + code).text
    soup = BeautifulSoup(source, 'lxml')
    mainData = soup.find('div', class_='card-header')
    lastStatus = mainData.find('h2').text
    listItems = mainData.find_all('li')
    items = [lastStatus]
    for li in listItems:
        items.append(li.get_text())