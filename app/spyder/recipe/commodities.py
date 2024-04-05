"""
@author David Antilles
@description 商品解析
@timeSnapshot 2024/4/4-21:19:32
"""
import json

from bs4 import BeautifulSoup

with open('commodities.html', 'r', encoding='utf-8') as file:
    html = BeautifulSoup(file.read(), 'lxml')
    links = html.select(".border-box .clean-link")
    commodities_ll = []
    for i in range(len(links)):
        link: BeautifulSoup = links[i]
        p = link.select_one('p').string
        name = link['href']
        commodities_ll.append({
            'name': p,
            'link': name
        })
    print(commodities_ll)
