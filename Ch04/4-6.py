"""
날짜 : 2020/08/11
이름 : 유효진
내용 : 머신러닝 - 로지스틱 회귀 분석
"""
from sklearn.linear_model import LogisticRegression

#훈련데이터
train_data = [[40, 30], [30, 80], [20, 70], [70, 40], [60, 20]]
train_label = [+1, -1, -1, +1, +1]

#모델학습
model = LogisticRegression()
model.fit(train_data, train_label)

#모델검증
result = model.predict(train_data)
print('result :', result)

#새로운 데이터 검증
test_data = [[46.12, 62.53], [27.20, 45.12], [37.15, 51.22]]
test_result = model.predict(test_data)
print('test_result :', test_result)
