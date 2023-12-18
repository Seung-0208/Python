'''
[requests로 요청해서 환율 크롤링하기]
- https://finance.naver.com/marketindex/
1. requests로 요청 보내기
2. 응답바디에서 beautifulSoup 사용해 필요한 데이터 스크래핑
    📍팁] css selector 사용해서 데이터 읽어올 때 - 페이지 > 검사 > 필요한 태그 우클릭 > copy css selector 클릭
'''

from bs4 import BeautifulSoup
import requests

#요청 보내기
url = 'https://finance.naver.com/marketindex/'
source = requests.get(url).text

#css셀렉터 사용해서 환율 정보 스크래핑
soup = BeautifulSoup(source,'html.parser')
#달러 환율 가져오기
dollars = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
#엔화 환율 가져오기
#- ⚠️처음 가지고 온 url에는 jpy가 비활성화 되어 있으므로 li.on에서 on을 빼줘야 함
yen = soup.select_one('#exchangeList > li > a.head.jpy > div > span.value')
print(f'1달러 환율:{dollars.text}원 | 100엔 환율:{yen.text}원')