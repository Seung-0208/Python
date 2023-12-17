'''
[requests모듈로 naver_news_api 사용하기]
- csv 모듈 사용
    - csv.DictWriter(f, fieldnames)
        (:param)f에 csv파일을 저장하며 fieldsnames에 저장된 값이 csv파일의 헤더가 됨
        (:return)DictWriter객체를 반환
    - DictWriter.writeheader()
        -> csv파일의 헤더 작성
    - DictWriter.writerows(Iterable 객체)
        (:param)인자로 전해준 iterable객체의 모든 요소를 csv파일에 작성해줌
        - 데이터 안에 콤마가 사용될 경우 double quotation으로 감싸짐
        - writerow는 한 줄만 작성해줌
    -
'''

import requests
import csv

#0. client id, client secret 키 가져오기 (naver developers 페이지의 application 확인)
client_id = "sM2rl8g11O1ZIPlSTYg4"
client_secret = "FCDdCIgJ5M"

#1. 검색어 입력받기
query = input('검색어를 입력하세요? ')

#2. url에 쿼리 스트링 전달 및 요청 보내기
url = f'https://openapi.naver.com/v1/search/news.json?query={query}'
res = requests.get(url, headers={'X-Naver-Client-Id':client_id,'X-Naver-Client-Secret':client_secret})
code = res.status_code
if code==200:
    #결과 확인
    print(res.json())
    print(type(res.json()))
    #csv파일로 저장
    item = res.json()['items']
    with open('naver_news.csv','w',encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f=f, fieldnames=list(item[0].keys()))
        writer.writeheader()
        writer.writerows(item)
else:
    print(f'에러발생:'+str(code))