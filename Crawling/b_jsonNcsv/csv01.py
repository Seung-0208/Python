'''
[csv 모듈]
- csv파일을 읽고 쓰기 위한 모듈
- 파이썬 객체 리스트를 csv파일로 저장하는 절차
    1. csv.writer(파일객체) - csv.writer객체 생성
        writer = csv.writer(f)
    2. writer.writerow(반복가능한 객체) - 한 행씩 csv파일에 파이썬 객체를 출력함
        - writer로 헤더 먼저 작성
        writer.writerow(['header1','header2',...'])
    3. writer.writerows(반복가능한 객체) - 파이썬 객체를 한꺼번에 출력함
        writer.writerows(records)
    (혹은)3. writer.writerow를 사용
        for record in records:
            writer.writerow(record)
- 파이썬 객체 딕셔너리를 csv파일로 저장하는 절차
    1. csv.DictWriter(파일객체,fieldnames) - DictWriter클래스 생성
        - fieldnames: 반복가능한객체,
            -dict의 키값과 fieldnames의 값은 정확히 일치해야 함!
             불일치 시 ValueError발생
            -fieldnames에 저장한 값이 헤더명이 됨
        writer = csv.DictWriter(f, fieldnames=['header1','header2',..])
    2. writer.writeheader() - csv파일의 헤더 작성
    3. writer.writerows(records) - 데이터 작성
    (혹은)3. writer.writerow를 사용
        for record in records:
            writer.writerow(record)
'''

import csv

#📌 리스트 -> csv 파일에 저장
records=[
    [1,'가길동','KIM','1234','가산동',25],
    [2,'나길동','LEE','1234','나산동',20],
    [3,'다길동','PARK','1234','다산동',30]
]

with open('users_list.csv','w',encoding='utf8', newline='') as f:
    writer = csv.writer(f)
    #print(dir(writer)) #writerow, writerows
    writer.writerow(['no','name','id','pwd','adr','age'])
    for record in records: #방법1
        writer.writerow(record)
    #writer.writerows(records) #빙법2

#📌 dict -> csv 파일에 저장
records=[
    {'번호':1,'이름':'가길동','아이디':'KIM','비번':'1234','주소':'가산동','나이':25},
    {'번호':2,'이름':'나길동','아이디':'LEE','비번':'1234','주소':'나산동','나이':35},
    {'번호':3,'이름':'다길동','아이디':'PARK','비번':'1234','주소':'다산동','나이':45}
]

with open('users_dict.csv','w', encoding='utf8', newline='') as f:
    writer = csv.DictWriter(f,fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)
    '''
    #혹은
    for record in records:
        writer.writerow(record)
    '''