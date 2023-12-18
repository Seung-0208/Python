'''
[BeautifulSoup 기초]
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- html이나 xml을 파싱할 때 주로 많이 사용하는 외부 라이브러리
- 사전작업 필요 | pip install bs4
- bs4.__version__ : bs의 버전 확인 가능
- BeautifulSoup(html, 'html.parser') - BeautifulSoup 객체 생성
    첫번째 인자 - html소스코드 혹은 파일 객체
    두번째 인자 - 사용할 parser명시

- BeautifulSoup의 이름공간 살펴보기
    [태그명으로 태그찾기]
    - soup.태그명 혹은 soup.find('태그명') : 제일 먼저 발견되는 해당 태그 요소 하나를 반환
        - 태그명은 반드시 소문자
        - 반환 타입 : <class 'bs4.element.Tag'>
    - soup('HTML태그명') : 태그명에 해당하는 모든 태그요소(Tag객체)를 리스트로 반환
        - 없으면 빈리스트 반환
    - soup.find_all('HTML태그명' [,limit=개수]) : 태그명에 해당하는 모든 태그요소(Tag객체)를 리스트로 반환
        - 📍limit=개수 를 인자로 전달 시 원하는 개수만 찾을 수 있음
        [태그 안에 들어있는 특정 문자열 찾기]
        - 📍'HTML태그명' 대신 string='특정문자열 혹은 정규표현식' 전달 시
            -> bs4.element.ResultSet타입의 결과값 반환
    [속성값으로 태그찾기]
    - [방법1] soup.find[_all](속성명='속성값')
      [방법2] soup.find[_all](name=None,attrs={'속성명':'속성값'})
        : 속성값으로 태그를 찾아 반환 (find은 하나만, find_all은 전부 반환)
        - (방법1) 속성명을 키워드 인수로 전달
            - 📍class 속성은 파이썬의 예약어이므로 class_ 로 지정해줘야 함
        - (방법2) 모든 태그를 대상으로 찾을 때는 name=None지정
    [CSS 셀렉터로 태그 찾기]
    - xpath는 지원 안함
    - soup.select('css셀렉터') = find_all()을 실행
    - soup.select_one('CSS셀렉터') = find()를 실행
- Tag객체의 이름공간 살펴보기 - BeautifulSoup의 이름공간과 유사
    - tag.name : 태그명 반환
    - tag.find_next_sibling() : tag의 형제태그 반환
        - tag.findNextSibling() - 이전 버전에서 사용된 함수
    - tag.string, tag.text, tag.get_text() : 시작태그와 종료태그 사이의 텍스트 추출
        - tag.string
            - 태그 사이에 텍스트가 없거나 하위 요소가 포함되어 있는 경우 None
            - 태그 사이에는 오직 텍스트만 있어야 함
        - tag.text, tag.get_text()
            - 태그 사이에 텍스트가 없는 경우 빈 문자열 반환
            - 하위요소가 포함되어 있더라도 하위요소에 포함된 모든 텍스트를 반환
    - tag['속성명'], tag.get('속성명'), tag.attrs['속성명'] : 속성명으로 속성값 읽어오기
        - class속성의 경우 공백으로 구분해서 여러개의 class 지정 가능 -> list가 반환됨
        - ⚠️tag객체가 가지고 있지 않은 속성명 전달 시
            tag['속성명'], tag.attrs['속성명'] - KeyError 발생
            tag.get('속성명') - None
'''

import re
from bs4 import BeautifulSoup
import bs4.element
import bs4

#BeautifulSoup 페이지에 나와있는 소스코드로 연습
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister family student" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<div><p>Hello, <b>Beautiful Soup</b>!</p></div>
<div></div>
<p class="story">...</p>
"""

#객체 생성
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify()) #보기 좋게 출력

#태그명으로 Tag 찾기
tag = soup.a #혹은 soup.find('a')
print(tag)
print(tag.name) #태그명 반환

#태그의 형제 태그 찾기
print(tag.find_next_sibling())

#태그 사이의 텍스트 추출하기
div = soup.div
print(f'string:{div.string}, text:{div.text}, get_text():{div.get_text()}')

#태그명에 해당하는 모든 태그 요소 찾기
tags = soup('a') #혹은 soup.find_all('a')
print(tags, type(tags), sep=' | ')

#태그명에 해당하는 태그들 중 원하는 개수만 찾기
tags = soup.find_all('a',limit=2)
print(tags, type(tags), sep=' | ')

#속성으로 태그 찾기
print('방법1 | id속성으로 찾기:',soup.find(id='link1'))
print('방법1 | class속성으로 찾기:',soup.find(class_='sister'))
print('방법2 | id속성으로 찾기:',soup.find(name=None, attrs={'id':'link1'}))
print('방법2 | class속성으로 찾기:',soup.find(name=None, attrs={'class':'sister'}))
print('특정 class속성에 해당하는 모든 태그 찾기:',soup.find_all(name=None, attrs={'class':'sister'}))

#시작태그와 종료 태그 사이의 텍스트에서 특정 문자열 찾기 - 찾고자 하는 문자열 그대로 전달
results = soup.find_all(string="The Dormouse's story")
print(results) #["The Dormouse's story", "The Dormouse's story"]
#ResultSet의 상속관계 확인
print(type(results)) #<class 'bs4.element.ResultSet'>
print(isinstance(results, list)) #True
#NavigableString의 상속관계 확인
print(type(results[0])) #<class 'bs4.element.NavigableString'>
print(isinstance(results[0], str)) #True

#시작태그와 종료 태그 사이의 텍스트에서 특정 문자열 찾기 - 정규표현식 사용
results = soup.find_all(string=re.compile(r'.+ie'))
print(f'results:{results}, type:{type(results)}')

#CSS 셀렉터로 태그 요소 찾기
print('css셀렉터로 태그 찾기(모두):',soup.select('p > a'))
print('css셀렉터로 태그 찾기(하나만):',soup.select_one('p > a'))

#특정 속성명의 속성값 읽어오기
a = soup.a
print(a['href'], a.get('href'), a.attrs['href'], sep=' | ') #모두 동일
print(a.get('title')) #없는 속성 읽어올 시 get만 None 반환, 나머지는 KeyError
print(a.get('class')) #class 속성값이 여러개인 경우 ['sister', 'family', 'student']
a_ = a.find_next_sibling()
print(a_.get('class')) #class 속성값이 한개인 경우 ['sister']