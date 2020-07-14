"""
    날짜 : 2020/07/14
    이름 : 유효진
    내용 : 파이썬 엑셀파일 데이터 출력
"""
import openpyxl

#엑셀파일 열기
fname = './naver.xlsx'
workbook = openpyxl.load_workbook(fname)

#첫번째 시트 선택
sheet = workbook.worksheets[0]

#시트의 각 행을 순서대로 출력
for row in sheet.rows:
    print('%s, %s, %s' % (row[0].value, row[1].value, row[2].value))