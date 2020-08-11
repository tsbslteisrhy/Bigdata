"""
날짜 : 2020/08/11
이름 : 유효진
내용 : 머신러닝 - 다중선형회귀 분석 연습문제
"""
from sklearn.linear_model import LinearRegression

#학습데이터(data: 키, 나이, 성별/ label: 몸무게)
train_data = [[170, 30, 1], [155, 60, 2], [150, 50, 2], [175, 40, 1], [165, 20, 1]]
train_label = [65, 50, 45, 70, 55]

#학습하기
model = LinearRegression()
model.fit(train_data, train_label)

#모델검증
test_data = [[172, 27, 1], [172, 27, 2]]
result = model.predict(test_data)
print('result :', result)