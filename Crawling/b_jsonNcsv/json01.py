'''
[json 라이브러리]
- 파이썬 2.6부터 표준 라이브러리로 제공
- 파이썬 객체를 JSON 형태의 문자열로 반환 | dump(), dumps()
    dump(json_object, fp) : json문자로 변환한 결과를 파일에 바로 쓰고 싶은 경우 사용
        (:param)json_object: 변환하고자 하는 파이썬 객체
        (:param)fp: 파일 객체
        (:param)indent = 4: 인덴트가 적용된 json형태의 문자열 반환(예쁘게 출력하기 위함)
            4는 들여쓰기를 4번 하라는 뜻. 변경 가능.
        (:return)None
    dumps(json_object) : json문자로 변환한 결과를 str타입으로 반환
        (:param)json_object: 변환하고자 하는 파이썬 객체
        (:param)ensuer_ascii=False : 한글을 유니코드값으로 인코딩하지 않아도 안꺠지도록 설정
        (:param)indent = 4: 인덴트가 적용된 json형태의 문자열 반환(예쁘게 출력하기 위함)
            4는 들여쓰기를 4번 하라는 뜻. 변경 가능.
        (:return)str
    loads(json_str) : json형태의 문자열을 딕셔너리 객체로 변환함
        (:param)json형태의 문자열
        (:return)딕셔너리 타입
'''

import json

#파이썬 객체를 json 형태의 문자열로 반환 = json 인코딩
dic = dict(zip(('id','pwd''name','age'),('kim','1234','김길동',20)))
dic_json = json.dumps(dic, ensure_ascii=False, indent=4)
print(dic_json) #결과값 확인용
print(type(dic_json)) #<class 'str'>

#json형태의 문자열을 파이썬 객체(딕셔너리)로 변환하기 = json 디코딩
dic_new = json.loads(dic_json)
print(dic_new)
print(dic_new['id'])


#💩json.loads()함수를 사용하지 않을 경우(str함수만으로 일일히 파싱해야 함)
split_ = dic_json.split(',') #['{\n    "id": "kim"', '\n    "pwdname": "1234"', '\n    "age": "김길동"\n}']
dic_nogada = {}
for index, element in enumerate(split_):
    if index==0: #첫번쨰 요소인 경우 {\n    "id": "kim"
        key = element.split(':')[0][1:].strip().replace('"','') #[1:] -> {를 없애줌
        value = element.split(':')[1].strip().replace('"','')
    elif index==len(split_)-1: #마지막 요소인 경우 \n    "age": "김길동"\n}
        key = element.split(':')[0].strip().replace('"','')
        value = element.split(':')[1][:-1].strip().replace('"','') #[:-1] -> }를 없애줌
    else: #나머지 요소들
        key = element.split(':')[0].strip().replace('"', '')
        value = element.split(':')[1].strip().replace('"', '')
    dic_nogada[key] = value

print(dic_nogada)

