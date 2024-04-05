"""
@author David Antilles
@description 食物爬虫
@timeSnapshot 2024/3/29-11:35:43
"""


from bs4 import BeautifulSoup

with open('food.html', 'r', encoding='utf-8') as file:
    html = file.read()
    soup = BeautifulSoup(html, 'lxml')
    ul = soup.select('ul')
    target = ul[9:14]
    pages = []
    for u in target:
        value_a = u.select("li a")
        page = []
        for a in value_a:
            page.append(a['title'])
        pages.append(page)
    print(pages)
