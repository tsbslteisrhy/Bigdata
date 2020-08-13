"""
날짜 : 2020/08/13
이름 : 유효진
내용 : 머신러닝 - 나이브베이즈 알고리즘 실습
"""
import pandas as pd
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

#데이터프레임 생성
df_iris = pd.read_csv('./data/iris.csv')

#학습데이터 준비
iris_data = df_iris.iloc[:, 0:4]
iris_label = df_iris.iloc[:, 4]

#훈련데이터와 테스트데이터로 분류
train_data, test_data, train_label, test_label = train_test_split(iris_data, iris_label)

#학습하기
model = GaussianNB()
model.fit(train_data, train_label)

#검증하기
result = model.predict(test_data)

#학습률 확인
score = metrics.accuracy_score(test_label, result)
print('학습률 :', score)