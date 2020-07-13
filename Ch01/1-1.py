"""
    날짜 : 2020/07/13
    이름 : 유효진
    내용 : 파이썬 HTML 요청하기
"""
import urllib.request as req

#네이버 HTML문서 요청
resp = req.urlopen('http://naver.com').read()
html = resp.decode('UTF-8')
print(html)