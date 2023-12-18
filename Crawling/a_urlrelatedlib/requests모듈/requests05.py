'''
[requests모듈 - post방식으로 요청 보내기]
- 방법1) requests.post(url)
- 방법2) requests.request('POST', url)



- 세션이 필요한 post 요청 보내기 (세션 객체를 사용하여 사용자의 세션 데이터를 저장하고 관리하는 경우)
    -> key=value쌍으로 저장됨
    (Spring Security를 사용한 로그인 페이지 사용 - 이전에 만들어놓은 페이지)
    -> http://localhost:9090/onememo/auth/LoginProcess.do 로 요청 보내기
    -> id, pwd에 대한 정보 전달
    📌 [방법]
    1. session = requests.Session() -> 세션객체 얻기
    2. session.post() -> 세션 객체로 요청 보내기
        -> Response객체 반환

- 세션이 필요없는 post 요청 보내기
    (이전에 만들어놨던 rest api사용 - 사용자 정보 추가)
    -> http://localhost:8080/users 로 요청 보내기
    -> username, password, name에 대한 정보 전달
    📌 [방법]
    - 방법1) urllib.requests모듈 사용
        - json으로 보낼 때
            req = urllib.request.Request(url, data=json.dumps({딕셔너리}), headers = 'content-type':'application/json'})
            urllib.request.urlopen(req)
        - key=value쌍으로 보낼 때
            data = urllib.request.parse.urlencode({딕셔너리})
            urllib.request.urlopen(f'{url}?{data}')
            (혹은) key=value&key=value.. 로 문자열을 연결해서 보내도 됨
    - 방법2) 📌 requests모듈 사용
        - json으로 보낼 때 - 헤더 안씀
            requests.post(url, json={딕셔너리})
        - key=value쌍으로 보낼 때
            requests.post(url, data={딕셔너리})
'''

import requests
#[세션이 필요한 post요청 보내기]
session = requests.Session()
url = 'http://localhost:9090/onememo/auth/LoginProcess.do'
res = session.post(url, data={'id':'KIM','pwd':'1234'}) #세션 객체로 post
#결과 확인
print('요청방식:',res.request.method)
print('상태코드:',res.status_code)
print('응답헤더:',res.headers)
print('응답바디(html소스):',res.text)

#[세션이 필요없는 post요청 보내기]
res = requests.post(url='http://localhost:8080/users', json={'username':'jfj','password':'1234','name':'피피피'})
print('응답바디:',res.text)
