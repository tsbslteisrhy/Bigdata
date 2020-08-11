"""
날짜 : 2020/08/11
이름 : 유효진
내용 : 머신러닝 - 선형회귀 분석 실습하기
"""
from scipy import stats
from sklearn.linear_model import LinearRegression

#학습데이터
x_data = [170, 155, 150, 175, 165]
y_data = [65, 50, 45, 70, 55]

#경사하강법으로 기울기, 절편 구하기
slope, intercept, r, p, std = stats.linregress(x_data, y_data)
print('기울기 :', slope)
print('y절편 :', intercept)


#학습데이터 (data: 키/ label: 몸무게)
train_data = [[170], [155], [150], [175], [165]]
train_label = [65, 50, 45, 70, 55]

#학습하기
model = LinearRegression()
model.fit(train_data, train_label)

#검증하기
test_data = [[180], [182], [173], [190], [188]]
result = model.predict(test_data)
print('result :', result)