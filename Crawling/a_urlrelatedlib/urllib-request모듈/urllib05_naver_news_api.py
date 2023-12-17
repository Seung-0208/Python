'''
네이버 개발자 센터 > Documents > 서비스 api > 검색 > 뉴스 - json 반환 url 사용
- query 파라미터 전달 필수
- 요청 헤더에 클라이언트 아이디와 클라이언트 시크릿 추가
'''

import urllib.parse as parse
import urllib.request as request

#0. client id, client secret 키 가져오기 (naver developers 페이지의 application 확인)
client_id = 'Client ID'
client_secret = 'Client Secret'

#1. 검색어 입력받기
query = input('검색어를 입력하세요? ')

#2. url에 쿼리 스트링 전달
url = f'https://openapi.naver.com/v1/search/news.json?{parse.urlencode({'query':query})}'
print(url)

#3. 요청 보내기
req = request.Request(url, headers={'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret})
resp = request.urlopen(req)
code = resp.status
if(code==200):
    print(resp.read().decode('utf8'))
else:
    print('에러발생:',code)