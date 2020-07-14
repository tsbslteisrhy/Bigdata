"""
    날짜 : 2020/07/14
    이름 : 유효진
    내용 : 파이썬 엑셀 저장하기
"""
from openpyxl import Workbook

#새로운 엑셀파일 생성
workbook = Workbook()

#현재 active sheet 열기
sheet = workbook.active

sheet['A1'] == '숫자'
sheet.append([1, 2, 3])
sheet.append(['사과', '배', '포도'])
sheet.cell(5, 5, '5행 5열 데이터')

#엑셀파일 저장
workbook.save('./test.xlsx')
workbook.close()

print('완료')