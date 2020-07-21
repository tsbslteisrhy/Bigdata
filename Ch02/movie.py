"""
    날짜 : 2020/07/16
    이름 : 유효진
    내용 : 파이썬 네이버 영화 리뷰평점 데이터 수집하기
"""
import os
import requests as req
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from datetime import datetime
from pymongo import MongoClient as mongo
import time

#크롬 가상브라우저 실행
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')
#browser = webdriver.Chrome('../Ch01/chromedriver.exe', chrome_options=chrome_options)
browser = webdriver.Chrome('../Ch01/chromedriver.exe')
browser.implicitly_wait(3)

# 랭크 페이지 번호 변수 선언
page = 1

# 1차:랭크 페이지
while True:

    # 랭크 변수 선언(0 ~ 49)
    i = 0
    time.sleep(1)

    while True:
        #네이버 영화 랭킹 평점순 이동
        browser.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200720&page='+str(page))
        browser.implicitly_wait(3)

        try:
            #영화 랭킹 클릭
            ranks = browser.find_elements_by_css_selector('#old_content > table > tbody > tr > td.title > div > a')
            ranks[i].click()
            browser.implicitly_wait(3)
        except:
            break

        #영화 평점 탭 클릭
        review_tab = browser.find_element_by_css_selector('#movieEndTabMenu > li:nth-child(5) > a')
        review_tab.click()
        browser.implicitly_wait(3)

        #영화제목 수집
        tit_tag = browser.find_element_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > h3 > a')
        href = tit_tag.get_attribute('href')
        i = href.rfind('=')+1

        code = href[i:]
        title = tit_tag.text

        # 평점, 리뷰, 날짜 수집을 위해 현재 브라우저를 iframe 페이지로 전환
        browser.switch_to.frame('pointAfterListIframe')
        browser.implicitly_wait(3)

        # 최신순 클릭
        tag_latest_a = browser.find_element_by_css_selector('#orderCheckbox > ul.sorting_list > li:nth-child(2) > a')
        tag_latest_a.click()
        browser.implicitly_wait(3)

        #MongoDB 접속, DB선택, Collection선택
        conn = mongo('mongodb://rhj:1234@192.168.100.101:27017')
        #conn = mongo('mongodb://rhj:1234@192.168.50.82:27017/rhj')
        db = conn.get_database('rhj')
        collection = db.get_collection('movie_score4')

        #현재 페이지 설정
        page_num = 1

        while True:

            try:
                # page 클릭(페이지 끝나면 클릭할 수 없어서 에러 발생: try ~ except)
                page_id = 'pagerTagAnchor'+str(page_num)
                page_btn = browser.find_element_by_id(page_id)
                page_btn.click()
                browser.implicitly_wait(3)
            except:
                break

            # 평점, 리뷰, 날짜 수집
            li_tags = browser.find_elements_by_css_selector('body > div > div > div.score_result > ul > li')
            list_data = []

            for li in li_tags:
                score = li.find_element_by_css_selector('.star_score > em')
                reple = li.find_element_by_css_selector('.score_reple > p > span:last-child')
                rdate = li.find_element_by_css_selector('.score_reple > dl > dt > em:nth-child(2)')

                list_data.append({'title': title,
                                  'code': code,
                                  'score': score.text,
                                  'reple': reple.text,
                                  'rdate': rdate.text})

            #Insert 실행
            collection.insert_many(list_data)

            print(page_num, '페이지 insert 완료.')
            page_num += 1

        # 그 다음 영화 리뷰 수집을 위한 랭크 변수 증가
        i += 1

    page += 1

print('종료...')

#브라우저 종료
browser.close()
browser.quit()