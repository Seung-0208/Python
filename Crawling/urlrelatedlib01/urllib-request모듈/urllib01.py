'''
[urllib.request 모듈 사용해서 웹 상의 데이터 읽어오기]
- 방법1) urlopen() 함수 사용
    - str타입의 url 주소 혹은 Request 객체 타입을 인자로 받음
        - request.urlopen('url 주소') 혹은 request.urlopen(Request객체)
    - 웹에서 얻은 데이터에 대한 객체 반환 (<class 'http.client.HTTPResponse'> 타입 반환)
    - HTTPResponse객체의 read()메소드로 html 소스를 얻을 수 있음
- 방법2) urlretrieve() 함수 사용
    - url 주소와 다운받을 파일명을 인자로 전달
    - tuple타입 반환 ('파일명', '응답헤더(HTTPMessage)')
    - html 소스를 파일로 다운받을 수 있음
'''
import urllib.request as request
#방법1 urlopen()함수 사용---------------------------------------------------

res = request.urlopen('https://www.daum.net/') #daum페이지의 데이터 크롤링

#반환값에 대한 기본 정보
print(f'value:{res}, type:{type(res)}') #urlopen함수의 반환 값 확인용
print('응답코드',res.status) #응답 코드
#print('응답헤더 얻는 방법1',res.headers)
print('응답헤더 얻는 방법2',res.getheaders()) #리스트로 반환
print('응답헤더 얻는 방법3',res.getheader('Content-Type')) #특정 헤더값만 받기

#response객체로부터 데이터 읽어오기
#이때 데이터는 <class 'bytes'> 타입이므로 decode() 과정이 필요함
#print(res.read())로 확인
source = res.read().decode()
print(source)

#파일에 저장하기
with open('daum_urlopen.html', 'w', encoding='utf8') as f:
    f.write(source)

#방법2 urlretrieve()함수 사용----------------------------------------------

tuple_ = request.urlretrieve(url='https://www.daum.net/', filename='daum_urlretrieve.html')
print(tuple_) #urlretrieve함수의 반환값 확인
print(tuple_[1].items()) #반환값으로 받는 튜플의 두번째 인자가 응답헤더임을 확인