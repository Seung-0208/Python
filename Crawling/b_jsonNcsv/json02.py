'''
[json모듈의 함수를 사용해 jsonplaceholder에서 유저 데이터 받기]
- 요청 보낼 url : https://jsonplaceholder.typicode.com/users
    -> json 형태의 문자열이 반환됨
        - json.loads()함수 사용
        - requests모듈에 내장된 json()함수 사용
'''

import  requests
import  json

res = requests.get('https://jsonplaceholder.typicode.com/users')
