'''
[csv파일에서 읽은 데이터를 파이썬 객체에 저장]
- csv.reader(파일객체) - Reader객체 반환
    - (기본) list(반환받은 Reader객체) -> 리스트를 요소로 갖는 리스트 반환. 즉, csv 데이터를 리스트 형태로 저장
    (응용) -> 위의 리스트의 첫번째 리스트는 헤더, 나머지는 데이터임을 고려하여
       dict를 요소로 갖는 리스트 생성 가능
'''

import csv

list_ = [] #요소가 리스트인 리스트
dict_ = [] #요소가 dict인 리스트

with open('users_list.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f)
    records = list(reader)
    print(records)
    header = records[0]
    body = records[1:]
    for record in body: #record 예. ['1', '가길동', 'KIM', '1234', '가산동', '25']
        list_.append(body) #헤더명이 없는 것 빼고는 records와 동일
        dict_.append(dict(zip(header,record)))

print(list_)
print(dict_)

