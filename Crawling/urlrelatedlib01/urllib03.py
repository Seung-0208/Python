'''
[urllib.request 모듈 사용해서 프로그램으로 구글 검색 이용하기]
1. 사전작업 requests모듈 설치
    터미널 창에서 pip install requests
2. 사용자로부터 검색어 입력받기
3. url에 쿼리스트링을 붙여 요청 전달
    - 이때 url에 한글이 포함되면 UnicodeEncodeError 발생 -> urllib.parse 모듈 사용
        1) parse.quote('한글') -> 빈 공백이 %20으로 인코딩됨
        2) parse.quote_plus() -> 빈 공백이 +로 인코딩됨 (권장)

[parse 모듈의 내장함수]
- parse.urlsplit(주소)
    -> url을 각 부분으로 나눠 SplitResult객체 반환
    -> SplitResult(scheme=' ', netloc=' ', path=' ', query=' ',..)
- parse.urlunsplit(SplitResult객체)
    -> SplitResult객체로 분리된 url을 다시 합쳐서 반환
- parse.urlencode(딕셔너리)
    -> 딕셔너리를 쿼리 스트링으로 반환
'''

#필요한 모듈 import
import urllib.request as request
import urllib.parse as parse

#방법1 urlopen()함수 사용---------------------------------------------------

query = input('검색어를 입력하세요?') #검색어 입력받기
encoded_query = parse.quote_plus(query)#한글로 입력된 검색어를 인코딩 (parse.quote_plus() 사용)
url = f'https://www.google.com/search?q={encoded_query}' #입력받은 검색어를 url에 쿼리스트링으로 전달
req = request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
res = request.urlopen(req) #생성된 Request객체 전달
with open('google.html','w',encoding='utf8') as f:
    f.write(res.read().decode())

#추가) parse 모듈 함수 사용해보기---------------------------------------------
urls = parse.urlsplit(url) #parse.urlsplit() : url을 각 부분으로 나누기
print(urls) #SplitResult(scheme='https', netloc='www.google.com', path='/search', query='q=%EB%89%B4%EC%A7%84%EC%8A%A4', fragment='')
print(parse.urlunsplit(urls))

#방법2 urlencode(딕셔너리)함수 사용-------------------------------------------
url = f'https://www.google.com/search?{parse.urlencode({'q':query,'oq':query})}'
req = request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
res = request.urlopen(req)
with open('google_.html','w', encoding='utf8') as f:
    f.write(res.read().decode())