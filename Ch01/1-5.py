"""
    날짜 : 2020/07/13
    이름 : 유효진
    내용 : 파이썬 가상 웹브라우저 실습하기
"""
from selenium import webdriver

#크롬 가상브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

#네이버 이동
browser.get('http://naver.com')

#로그인 버튼 클릭
login_btn = browser.find_element_by_css_selector('#account > a')
login_btn.click()

#아이디, 비밀번호 입력
input_id = browser.find_element_by_css_selector('#id')
input_pw = browser.find_element_by_css_selector('#pw')

input_id.send_keys('tsbslteisrhy')
input_pw.send_keys('')

#로그인 클릭
btn_submit = browser.find_element_by_css_selector('#log\.login')
btn_submit.click()