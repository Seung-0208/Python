'''
[외부 REST API 요청 (JSONPlaceHolder)]
https://jsonplaceholder.typicode.com/photos
- 위의 url로 요청 보내기 -> json 형태의 문자열이 반환됨
- json() : requests 모듈에 내장된, json형태의 문자열을 파이썬의 리스트 형태로 디코딩해주는 함수
    -> import json 불필요
'''

import requests

res = None