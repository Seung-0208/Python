'''
[requests모듈의 기초]
- urllib.request를 사용할 때와 달리 한글 인코딩 불필요
- 단 표준 라이브러리가 아니므로 설치 필요
- 요청 방식 - get 방식으로 요청한다고 가정
    - 방법1) requests.request(method='get', url='url', headers={})
    - 방법2) requests.get(url='url', headers={})
- 응답바디 인코딩 - response.encoding = 'utf-8'
- 응답에 대한 요청 객체 얻기 - req = res.request <class 'requests.models.PreparedRequest'>타입
=> [requests모듈을 사용해 daum페이지에 get방식으로 요청 보내기]
'''
#요청 보내기
import requests
res = requests.request('get',url='https://www.daum.net',headers={'User-Agent':'Mozilla/5.0'})
res.encoding = 'utf-8' #응답바디 인코딩

#응답 확인
print(f'응답코드: {res.status_code}')
print(f'응답헤더: {res.headers}')
print(f'응답바디-바이트문자열: {res.content}')
print(f'응답바디-문자열: {res.text}') #res.encoding='utf-8' 코드를 입력하지 않으면 한글이 다 깨짐
print(f'인코딩방식: {res.encoding}')

with open('daum_requests.html', 'w', encoding='utf8') as f:
    f.write(res.text)

#응답과 관련된 요청 객체 얻기
req = res.request
print(f'요청방식:{req.method}')
print(f'요청url:{req.url}')
print(f'요청헤더:{req.headers}')