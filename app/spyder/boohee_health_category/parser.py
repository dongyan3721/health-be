"""
@author David Antilles
@description 
@timeSnapshot 2024/3/31-17:27:14
"""
from bs4 import BeautifulSoup

CONTEXT = 'https://www.boohee.com'

with open('example.html', 'r', encoding='utf-8') as file:
    source = file.read()
    dom_selector = BeautifulSoup(source, 'lxml')
    print(type(dom_selector))
    ul = dom_selector.select_one('.food-list')
    for li in ul.select('li'):
        context_redirect = CONTEXT + li.select_one('.img-box a')['href']
        print(context_redirect)
