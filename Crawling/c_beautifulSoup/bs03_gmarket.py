'''
[지마켓에서 검색한 상품 스크래핑하기]
1. url에 요청 보내서 html소스 받아오기
2. html 소스에서 필요한 상품명과 가격 추출하기
'''

import requests
from bs4 import BeautifulSoup

#ui
query, qty = input('검색어와 스크래핑할 개수를 입력하세요(공백구분): ').split()
url = f'https://browse.gmarket.co.kr/search?keyword={query}'
#html소스
source = requests.get(url).text
soup = BeautifulSoup(source,'html.parser')

#상품명 불러오기
namesTag = soup.select("#section__inner-content-body-container > div:nth-child(4) > div > div > div.box__information > div.box__information-major > div.box__item-title > span > a > span.text__item", limit=int(qty))
print(len(namesTag))
names=[]
for name in namesTag:
    names.append(name.get_text())

#가격 불러오기
pricesTag = soup.select('#section__inner-content-body-container > div:nth-child(4) > div > div > div.box__information > div.box__information-major > div.box__item-price > div.box__price-seller > strong', limit=int(qty))
prices=[]
for price in pricesTag:
    prices.append(price.get_text())

for name, price in zip(names,prices):
    print(f'{name} : {price}')