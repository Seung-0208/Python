'''
[urllib.request 모듈 사용해서 get방식, post방식으로 요청 보내기]
- get 방식 : urlopen('url') 혹은 urlopen(Request객체)
- post 방식 : urlopen(Request(url, data=params, headers={}))
    - data라는 키워드가 들어가면 post
    - json형식으로 데이터 전송
        - 이때 json라이브러리의 dumps()메소드를 활용
            dumps() : 파이썬의 dict,list,tuple 등을 json형식의 문자열로 인코딩
'''

import urllib.request as request
import urllib.parse as parse

#스프링 restapi프로젝트 폴더 > controller 패키지 > RestApiController 참고
url = 'http://localhost:8080/users'

#GET방식 요청-------------------------------------------------
params = parse.urlencode({'id':'아이디','pwd':'비밀번호'}) #key=value쌍 전달
req = request.Request(f'{url}?{params}')
res = request.urlopen(req)
print(req.get_method())
print(res.status)
print(res.read().decode())

#POST방식 요청-------------------------------------------------
import json #json 형식으로 전달
params = json.dumps({
    'id':'na1234',
    'pwd':'na12341234!'
})
req = request.Request(url, data=params.encode(),headers={'content-type':'application/json'})
res = request.urlopen(req)
print(req.get_method())
print(res.status)
print(res.read().decode())