"""
날짜 : 2020/08/11
이름 : 유효진
내용 : 머신러닝 - 다중선형회귀 분석 실습하기
"""
from sklearn.linear_model import LinearRegression

#학습데이터 (data: 키, 나이/ label: 몸무게)
train_data = [[170, 30], [155, 60], [150, 50], [175, 40], [165, 20]]
train_label = [65, 50, 45, 70, 55]

#학습하기
model = LinearRegression()
model.fit(train_data, train_label)

#모델검증
test_data = [[178, 32], [167, 29], [185, 43]]
result = model.predict(test_data)
print('result :', result)