'''
[urllib.request 모듈 사용해서 웹 상의 이미지 읽어오기]
- urlretrieve() 함수와 urlopen() 함수 사용
- 'https://images.pexels.com/photos/3081487/pexels-photo-3081487.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'
    위의 링크에 있는 이미지 읽어오기
- 이때 그냥 읽어오면 Forbidden에러 발생
    -> 위의 오류를 해결하기 위해 프로그램이 아닌 브라우저가 요청한 것처럼 속여야 함
- request.urlopen(위의 url 주소) 호출 시
    -> Request객체를 생성하여 요청 헤더 추가
    -> urlopen의 인자로 위에서 생성한 Request객체 전달
- urlretrieve() 함수 호출 시
    -> request.build_opener()함수를 이용해 요청헤더의 설정값 수정
'''
import urllib.request as request

#방법1 urlopen()함수 사용---------------------------------------------------

url = 'https://images.pexels.com/photos/3081487/pexels-photo-3081487.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'
req = request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
res = request.urlopen(req)
binary = res.read() #이미지 읽기
with open('landscape1.jpeg','wb') as f:#이미지 파일 읽기 (이미지 파일이므로 바이너리 타입으로 읽어와야 함)
    f.write(binary) #읽어온 데이터를 파일에 저장

#방법2 urlretrieve()함수 사용----------------------------------------------

opener = request.build_opener()#opener객체 생성
opener.addheaders = [('User-agent', 'Mozilla/5.0')]#요청 헤더 값 설정
request.install_opener(opener)#바뀐 헤더 정보 적용
request.urlretrieve(url,filename='landscape2.jpeg')
