"""
    날짜 : 2020/07/13
    이름 : 유효진
    내용 : 네이버 실시간 검색어 출력하기
"""
import os
import requests as req
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from datetime import datetime

#크롬 가상브라우저 실행
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
browser.implicitly_wait(3)

#네이버 데이터랩 메인 이동
browser.get('https://datalab.naver.com/keyword/realtimeList.naver?where=main')
browser.implicitly_wait(3)

#네이버 실검 1~10위 파싱
item_boxs = browser.find_elements_by_css_selector('#content > div > div.selection_area > div.selection_content > div.field_list > div > div > ul:nth-child(1) > li > .item_box')

#디렉터리 생성
dir = "/home/bigdata/naver/naver-{:%y-%m-%d}".format(datetime.now())

if not os.path.exists(dir):
	os.makedirs(dir)

#파일로 저장
fname = "{:%y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(dir+'/'+fname, mode='w', encoding='utf8')

file.write('순위,제목,날짜\n')

for item in item_boxs:
    file.write('%s,' % item.find_element_by_css_selector('.item_num').text)
    file.write('[%s],' % item.find_element_by_css_selector('.item_title_wrap > .item_title').text)
    file.write('%s\n' % "{:%y%m%d%H%M%S}".format(datetime.now()))

#파일닫기
file.close()

#브라우저 종료
browser.close()
