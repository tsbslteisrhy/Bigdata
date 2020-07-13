"""
    날짜 : 2020/07/13
    이름 : 유효진
    내용 : 파이썬 데이터 전송 후 페이지 요청하기
"""
import requests as req
from bs4 import BeautifulSoup as bs

#세션시작
sess = req.session()

#로그인
id = 'ksb0503'
pw = '123456789'

login_check_url = 'https://here.busan.com/bbs/login_check.php'
sess.post(login_check_url, data={'mb_id': id, 'mb_password': pw})

#마이페이지 요청
html = sess.get('https://here.busan.com/member/member_mypage.php')

#파싱
dom = bs(html.text, 'html.parser')
point = dom.select_one('#design_contents > div.point > font:nth-child(2)')

print('현재 포인트 :', point.text)

