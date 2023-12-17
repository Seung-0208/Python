'''
[외부 REST API 요청 (JSONPlaceHolder)]
https://jsonplaceholder.typicode.com/photos - json을 요소로 갖는 리스트가 저장되어 있음
- 위의 url로 요청 보내기 -> json 형태의 문자열이 반환됨
- json() : requests 모듈에 내장된, json형태의 문자열을 파이썬의 리스트 형태로 디코딩해주는 함수
    -> import json 불필요
'''

import requests
import urllib.request
res = requests.get('https://jsonplaceholder.typicode.com/photos')
#json()의 반환값 확인
print(res.json())
print(type(res.json())) #<class 'list'>

photos = res.json()

#url을 사용해 이미지 3개만 다운받기
cnt = 0
for photo in photos:
    for key, value in photo.items():
        if key=='url' and cnt<3:
            cnt += 1
            #파일 다운 시 urlib.request.urlretrieve 사용
            urllib.request.urlretrieve(value,f'{value.split('/')[-1]}.png')
            
