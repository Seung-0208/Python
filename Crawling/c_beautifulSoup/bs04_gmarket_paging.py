'''
[쿠팡 쇼핑 상품 목록 정보 가져오기(함수버전-제너레이터 사용)]
- 페이징 번호 반영해서 크롤링하기
- 함수로 작성
    - start_requests()
        param)pages: 크롤링해올 페이지 번호
    - parse()
        param)url: 요청보낼 url
- yield와 제너레이터 : 특정값 반환 후 다시 반복문 안으로 들어옴
'''

from bs4 import BeautifulSoup
import requests
#요청 보내기
def start_requests(pages):
    '''
    :param pages: 끝 페이지 번호
    :yield: url에 따른 스크래핑 결과 반환
    '''
    keyword = input('검색어 입력: ')
    for page in range(1,pages+1):
        url = f'https://www.coupang.com/np/search?q={keyword}&channel=&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={page}&rocketAll=false&searchIndexingToken=1=9&backgroundColor='
        print(url)
        yield parse(url)

def parse(url):
    #요청 보내기
    user_agent = 'Mozilla/5.0'
    header = {'User-Agent':user_agent}
    source = requests.get(url, headers=header).text
    #필요한 태그 찾기
    soup = BeautifulSoup(source,'html.parser')
    names = soup.select('a > dl > dd > div > div')
    prices = soup.select('a > dl > dd > div > div.price-area > div > div.price > em > strong')
    return zip(names,prices)

if __name__ == "__main__":
    pages = int(input('마지막 페이지 번호 입력: '))
    products = start_requests(pages)
    for idx, product in enumerate(products): #한 페이지의 상품 목록이 product에 담김
        print(f'{idx+1}페이지의 상품 목록')
        for price, name in product:
            print(f'{name.get_text()} : {price.get_text()}')