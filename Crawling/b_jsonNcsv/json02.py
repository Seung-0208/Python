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
print(type(res.text)) #json 형태의 문자열 반환

#json모듈의 loads() 함수 사용
users = json.loads(res.text)
print(users) #dict타입의 요소를 갖는 list 반환
for user in users: #정리해서 출력
    for key, value in user.items():
        print(f'{key}:{value}', end='\t\t')
    print()

#requests에 내장된 json() 함수 사용
users = res.json()
print(users) #dict타입의 요소를 갖는 list 반환
for user in users: #정리해서 출력
    for key, value in user.items():
        print(f'{key}:{value}', end='\t\t')
    print()