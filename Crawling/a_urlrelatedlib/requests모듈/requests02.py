'''
[requests 모듈 사용해서 get방식으로 웹 상의 이미지 읽어오기]
1. url 요청
- 방법1) requests.get(url)
- 방법2) requests.request('GET', url)
2. 응답 값 읽기
- 이미지 파일이므로 res.content로 읽어와야 함

=> urllib.request모듈과의 차이점
    - urllib.request모듈 : 요청헤더에 'user-agent'값을 설정해주지 않으면 Forbidden에러 발생
    - requests모듈 : 요청헤더에 따로 설정해주지 않아도 Forbidden에러가 발생하지 않음
'''
import requests
url = 'https://images.pexels.com/photos/3081487/pexels-photo-3081487.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'
res = requests.get(url) #requests.request('get', url)과 같음
with open('landscape.jpeg', 'wb') as f:
    f.write(res.content)